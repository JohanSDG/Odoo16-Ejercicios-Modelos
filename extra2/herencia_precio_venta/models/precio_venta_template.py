from odoo import fields, models, api

class productTemplateHerencia(models.Model):
    _inherit = 'product.template'

    #needed_quality = fields.Char(string="Calidad Requerida")
    precio_venta2 = fields.Integer( string="Precio Venta 2")