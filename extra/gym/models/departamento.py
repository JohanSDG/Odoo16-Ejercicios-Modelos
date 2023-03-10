from odoo import api, models, fields

class Departamento(models.Model):
        _name = 'formulario_departamento_stargym'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nombre_departamento'
        nombre_departamento = fields.Char(string='Departamento')