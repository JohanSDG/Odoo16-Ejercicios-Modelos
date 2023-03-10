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
class formularioHospitalModels(models.Model):
    _name = 'hospitalcj_clientes_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Este formulario es para los clientes premium starbucks'
    nombre = fields.Char( string = 'Nombre Completo')
    apellido = fields.Char(string = 'Apellido Completo')
    tipoidentificacion = fields.Selection([ ('cedula', 'Cedula'),('dni', 'DNI'),('pasaporte', 'Identificacion Pasaporte')],string = 'seleccione Tipo Identificacion')
    numero_identificacion = fields.Integer(string = 'numero de identificacion')
    genero = fields.Selection([ ('hombre', 'Hombre'),('mujer', 'Mujer')], string='Seleccione su genero')
    fecha_nacimiento = fields.Date(string = 'Fecha Nacimiento')
    email = fields.Char(string = 'Correo Electronico')
    departamento_id = fields.Many2one('formulario_departamento_clinicacj', string='Departamento')
    municipio_id = fields.Many2one('formulario_municipio_clinicacj', string='Municipio')
    pais_id = fields.Many2one('formulario_pais_clinicacj',string='Pais')
    estado = fields.Selection([('draft', 'Borrador'),('confirmed', 'Confirmado'),('done', 'Realizado'),('cancelled', 'Cancelado')], string='Estado', default='draft', tracking=True)
    doctor = fields.Many2many('formulario_doctor_clinicacj',string = 'Asignar Doctor')
    #cita_medica = fields.Many2many('formulario_citamedica',string = 'Seleccione la cita que desea tomar') 
    observaciones = fields.Text(string = 'Obersevaciones a Resaltar')


# Metodos para cambiar el estado de las reservas y asignarla en el xml
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



class Departamento(models.Model):
        _name = 'formulario_departamento_clinicacj'
        _description = 'Este formulario es para los clientes del hospital javeriano'
        _rec_name = 'nombre_departamento'
        nombre_departamento = fields.Char(string='Departamento')
        


class Municipio(models.Model):
        _name = 'formulario_municipio_clinicacj'
        _description = 'Este formulario es para los clientes del hospital javeriano'
        _rec_name = 'nombre_municipio'
        nombre_municipio = fields.Char(string='Municipio')
        departamento_id = fields.Many2one('formulario_departamento_clinicacj', string='Departamento')


class Pais(models.Model):
        _name = 'formulario_pais_clinicacj'
        _description = 'Este formulario es para los clientes del hospital javeriano'
        _rec_name = 'nombre_pais'
        nombre_pais = fields.Char(string='pais')
     

class Doctor(models.Model):
        _name = 'formulario_doctor_clinicacj'
        _description = 'Este formulario es para los clientes del hospital javeriano'
        _rec_name = 'nombre_medico'
        nombre_medico = fields.Char(string='Nombre Completo')
        apellido = fields.Char(string = 'Apellido Completo')
        tipoidentificacion = fields.Selection([ ('cedula', 'Cedula'),('dni', 'DNI'),('pasaporte', 'Identificacion Pasaporte')],string = 'seleccione Tipo Identificacion')
        numero_identificacion = fields.Integer(string = 'numero de identificacion')
        genero = fields.Selection([ ('hombre', 'Hombre'),('mujer', 'Mujer')], string='Seleccione su genero')
        fecha_nacimiento = fields.Date(string = 'Fecha Nacimiento')
        email = fields.Char(string = 'Correo Electronico')
        departamento_id = fields.Many2one('formulario_departamento_clinicacj', string='Departamento')
        municipio_id = fields.Many2one('formulario_municipio_clinicacj', string='Municipio')
        especializacion = fields.Char(string='Digite su Especialidad')




        