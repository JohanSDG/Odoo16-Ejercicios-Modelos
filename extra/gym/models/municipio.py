from odoo import api, models, fields

class Municipio(models.Model):
        _name = 'formulario_municipio_stargym'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nombre_municipio'
        nombre_municipio = fields.Char(string='Municipio')
        departamento_id = fields.Many2one('formulario_departamento_stargym', string='Departamento')

