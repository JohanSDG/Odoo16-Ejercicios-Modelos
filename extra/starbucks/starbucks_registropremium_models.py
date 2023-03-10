#from odoo import api, models, fields
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

#Estamos definiendo los campos.
class formularioModels(models.Model):
    _name = 'starbucks_clientes_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Este formulario es para los clientes premium starbucks'
    nombre = fields.Char( string = 'Name')
    apellido = fields.Char(string = 'Last Name')
    tipoidentificacion = fields.Selection([ ('cedula', 'Identification'),('dni', 'DNI'),('pasaporte', 'Passport')],string = 'select identification type')
    numero_identificacion = fields.Integer(string = 'identification number')
    genero = fields.Selection([ ('hombre', 'men'),('mujer', 'women')], string='Seleccione su genero')
    fecha_nacimiento = fields.Date(string = 'Birth date')
    email = fields.Char(string = 'Email')
    departamento_id = fields.Many2one('formulario_departamento_starbucks', string='state')
    municipio_id = fields.Many2one('formulario_municipio_starbucks', string='municipality')
    pais_id = fields.Many2one('formulario_pais_starbucks',string='country')
    start_date = fields.Date(string='fecha ingreso', tracking=True, required=True)  # Fecha de inicio de la reserva
    end_date = fields.Date(string='fecha final', tracking=True, required=True)  # Fecha de fin de la reserva
    days_booked = fields.Integer(string='total dias', compute='_compute_calculo_dias', store=True)  # Número de días reservados
    #valor_reserva = fields.Float(string='Valor Reserva', compute='_compute_valor_reserva')  # Valor de la reserva
    estado = fields.Selection([('draft', 'Borrador'),('confirmed', 'Confirmado'),('done', 'Realizado'),('cancelled', 'Cancelado')], string='Estado', default='draft', tracking=True)
    observaciones = fields.Text(string = 'Obersevaciones a Resaltar')


    @api.depends('start_date', 'end_date')
    def _compute_calculo_dias (self):
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


# Metodos para cambiar el estado de las reservas y asignarla en el xml
    def confirmar_reservacion(self):
        self.ensure_one()
        self.state = 'confirmed'

    def mark_as_done(self):
        self.ensure_one()
        self.state = 'done'
    
    def cancelar_reservacion(self):
        self.ensure_one()
        self.state = 'cancelled'

    def change_borrador(self):
        self.ensure_one()
        self.state = 'draft'





class Departamento(models.Model):
        _name = 'formulario_departamento_starbucks'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nombre_departamento'
        nombre_departamento = fields.Char(string='Departamento')
        


class Municipio(models.Model):
        _name = 'formulario_municipio_starbucks'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nombre_municipio'
        nombre_municipio = fields.Char(string='Municipio')
        departamento_id = fields.Many2one('formulario_departamento_starbucks', string='Departamento')


class Pais(models.Model):
        _name = 'formulario_pais_starbucks'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nombre_pais'
        nombre_pais = fields.Char(string='pais')
        
       






        