from odoo import api, models, fields

class Entrenador(models.Model):
        _name = 'entrenador_modulos'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nombre_entrenador'
        nombre_entrenador = fields.Char(string='Nombre Entrenador')
        apellido = fields.Char(string='Nombre Entrenador')
        direccion = fields.Char(string='Direccion')
        telefono = fields.Integer(string='Telefono')