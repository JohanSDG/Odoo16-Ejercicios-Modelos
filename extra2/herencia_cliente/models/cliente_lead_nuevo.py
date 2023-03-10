from odoo import fields, models, api

class Contact(models.Model):
    _inherit = 'res.partner'

    #needed_quality = fields.Char(string="Calidad Requerida")
    telefono3 = fields.Char(string="Telefono 3")