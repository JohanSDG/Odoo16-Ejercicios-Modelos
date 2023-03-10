
from csv import Dialect
from email.policy import default
from re import S
from socket import TCP_NODELAY
from tkinter import dialog
from unittest import result
from odoo import api, models, fields, tools, exceptions, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero
from odoo.addons import bus


class ProductsBooking(models.Model):
    _name = 'products_booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'products_booking'

    _rec_name = 'number'
    number = fields.Char(string='Numero de reserva', index=True, copy=False, readonly=True, default=lambda  self: 'New')
    customer_id = fields.Many2one('res.partner', string='Customer', tracking=True, required=True)  # Cliente que realiza la reserva
    product_id = fields.Many2one('product.template', string='Product', tracking=True, required=True, domain=[('can_be_booked', '=', True)])
    fecha_inicio = fields.Date(string='Start Date', tracking=True, required=True)  # Fecha de inicio de la reserva
    fecha_final = fields.Date(string='End Date', tracking=True, required=True)  # Fecha de fin de la reserva
    dias_reservados = fields.Integer(string='Days Booked', compute='_compute_dias_reservados')  # Número de días reservados
    valor_reserva = fields.Float(string='Valor Reserva', compute='_compute_valor_reserva')  # Valor de la reserva
    state = fields.Selection([('draft', 'Borrador'),('confirmed', 'Confirmado'),('done', 'Realizado'),('cancelled', 'Cancelado')], string='Estado', default='draft', tracking=True)
    notes = fields.Text(string='notes')

    # Agregar la secuencia para Modulo de Booking
    @api.model
    def create(self, vals_list):
        if vals_list.get('number', 'New') == 'New':
            vals_list['number'] = self.env['ir.sequence'].next_by_code('products_booking.sequence') or 'New'
        result = super(ProductsBooking, self).create(vals_list)
        return result

    # Metodos para cambiar el estado de las reservas 
    def confirm_reservation(self):
        self.ensure_one()
        self.state = 'confirmed'

    def mark_as_done(self):
        self.ensure_one()
        self.state = 'done'
    
    def cancel_reservation(self):
        self.ensure_one()
        self.state = 'cancelled'

    def change_to_draft(self):
        self.ensure_one()
        self.state = 'draft'

    # Permite verificar que el numero de dias de la reserva y que la fecha de salida no sea inferior al ingreso
    # Tambien que la reserva minima sea un dia, si la fecha de ingreso y salida es el mismo Dia
    @api.depends('fecha_inicio', 'fecha_final')
    def _compute_dias_reservados(self):
        for record in self:
            if record.fecha_inicio and record.fecha_final:
                fecha_inicio = fields.Datetime.from_string(record.fecha_inicio)
                fecha_final = fields.Datetime.from_string(record.fecha_final)
                if fecha_inicio == fecha_final:
                    record.dias_reservados = 1
                else:
                    record.dias_reservados = int((fecha_final - fecha_inicio).days)
            else:
                record.dias_reservados = 1

    @api.depends('dias_reservados', 'product_id.list_price')
    def _compute_valor_reserva(self):
        for record in self:
            record.valor_reserva = record.dias_reservados * record.product_id.list_price

    @api.onchange('fecha_final')
    def onchange_fecha_final(self):
        if self.fecha_inicio and self.fecha_final and self.fecha_inicio > self.fecha_final:
                return {'warning': {
                'title': _("Revisa la fecha de ingreso y salida"),
                'message': ('La fecha de CheckOut debe ser posterior a la fecha de CheckIn')}}


# Verificar que la feha de la rerva no debe ser anterior a al fecha actual
    @api.onchange('fecha_inicio')
    def _check_fecha_inicio(self):
        if self.fecha_inicio and self.fecha_inicio < fields.Date.today():
            self.fecha_inicio = fields.Date.today()
         