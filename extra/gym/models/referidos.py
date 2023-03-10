from odoo import api, models, fields

class Referidos(models.Model):
        _name = 'referidos_models'
        _description = 'Este formulario es para los clientes premium starGym'
        _rec_name = 'nombre_referido'
        nombre_referido = fields.Char(string='Nombre')
        apellido_usuario = fields.Char(string='Apellido')