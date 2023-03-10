from odoo import api, models, fields

class Pais(models.Model):
        _name = 'formulario_pais_stargym'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nombre_pais'
        nombre_pais = fields.Char(string='pais')