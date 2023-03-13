# -*- coding: utf-8 -*-
from odoo import api, models, fields, tools, exceptions, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero
from odoo.addons import bus


class ProductsBooking(models.Model):
    _name = 'coworking_booking'
    _description = 'coworking_booking'

    _rec_name = 'number'
    number = fields.Char(string='reservation number', index=True, copy=False, readonly=True, default=lambda  self: 'New')
    customer_id = fields.Many2one('res.partner', string='Customer ', tracking=True, required=True)  # Cliente que realiza la reserva
    tipeidentification = fields.Selection([ ('cedula', 'Cedula'),('dni', 'DNI'),('pasaporte', 'Identificacion Pasaporte')],string = 'select identification type')
    number_identification = fields.Integer(string = 'Number Identification')
    product_id = fields.Many2one('product.template', string='Product Hotel')
    start_date = fields.Date(string='Start Date', tracking=True, required=True)  # Fecha de inicio de la reserva
    end_date = fields.Date(string='End Date', tracking=True, required=True)  # Fecha de fin de la reserva
    days_booked = fields.Integer(string='Days Booked', compute='_compute_days_booked')  # Número de días reservados
    valor_reserva = fields.Float(string='Valor Reserva', compute='_compute_valor_reserva')  # Valor de la reserva
    state = fields.Selection([('draft', 'Borrador'),('confirmed', 'Confirmado'),('done', 'Realizado'),('cancelled', 'Cancelado')], string='Estado', default='draft', tracking=True)
    notes = fields.Text(string='notes')


    
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
    @api.depends('start_date', 'end_date')
    def _compute_days_booked(self):
        for record in self:
            if record.start_date and record.end_date:
                start_date = fields.Datetime.from_string(record.start_date)
                end_date = fields.Datetime.from_string(record.end_date)
                if start_date == end_date:
                    record.days_booked = 1
                else:
                    record.days_booked = int((end_date - start_date).days)
            else:
                record.days_booked = 1

    @api.depends('days_booked', 'product_id.list_price')
    def _compute_valor_reserva(self):
        for record in self:
            record.valor_reserva = record.days_booked * record.product_id.list_price

    @api.onchange('end_date')
    def onchange_end_date(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
                return {'warning': {
                'title': _("Revisa la fecha de ingreso y salida"),
                'message': ('La fecha de CheckOut debe ser posterior a la fecha de CheckIn')}}


# Verificar que la feha de la rerva no debe ser anterior a al fecha actual
    @api.onchange('start_date')
    def _check_start_date(self):
        if self.start_date and self.start_date < fields.Date.today():
            self.start_date = fields.Date.today()
         