# -*- coding: utf-8 -*-
from odoo import api, models, fields, tools, exceptions, _

class Products(models.Model):
    _name = 'products_booking'
    _description = 'products_booking'
    
    usuario_id = fields.Many2one('res.partner', string='Customer')  # Cliente que realiza la reserva
    product_id = fields.Many2one('product.template', string='Product')
    inicio_fecha = fields.Date(string='Fecha Inicio', tracking=True, required=True)  # Fecha de inicio de la reserva
    final_fecha = fields.Date(string='Fecha Final', tracking=True, required=True)  # Fecha de fin de la reserva
    dias_reservados = fields.Integer(string='Dias Reservados', compute='_compute_buscar_reservas')  # Número de días reservados
    #valor_reserva = fields.Float(string='Valor Reserva', compute='_compute_valor_reserva')  # Valor de la reserva
    estado = fields.Selection([('draft', 'Borrador'),('confirmed', 'Confirmado'),('done', 'Realizado'),('cancelled', 'Cancelado')], string='Estado', default='draft', tracking=True)
    notes = fields.Text(string='notes')
    lugar_pais = fields.Many2one('formulario_pais_reserva', 'Esocoja Su Pais')

    # Metodos para cambiar el estado de las reservas 
    def confirmar_reservacion(self):
        self.ensure_one()
        self.estado = 'confirmed'

    def mark_as_done(self):
        self.ensure_one()
        self.estado = 'done'
    
    def cancelar_reservacion(self):
        self.ensure_one()
        self.estado = 'cancelled'

    def change_borrador(self):
        self.ensure_one()
        self.estado = 'draft'

    # Permite verificar que el numero de dias de la reserva y que la fecha de salida no sea inferior al ingreso
    # Tambien que la reserva minima sea un dia, si la fecha de ingreso y salida es el mismo Dia
    @api.depends('inicio_fecha', 'final_fecha')
    def _compute_buscar_reservas(self):
        for record in self:
            if record.inicio_fecha and record.final_fecha:
                inicio_fecha = fields.Datetime.from_string(record.inicio_fecha)
                final_fecha = fields.Datetime.from_string(record.final_fecha)
                if inicio_fecha == final_fecha:
                    record.dias_reservados = 1
                else:
                    record.dias_reservados = int((final_fecha - inicio_fecha).days)
            else:
                record.dias_reservados = 1


class Pais(models.Model):
        _name = 'formulario_pais_reserva'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'pais'
        pais = fields.Char(string='Pais')