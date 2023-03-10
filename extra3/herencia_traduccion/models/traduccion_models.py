from odoo import models, fields

class ResPartner(models.Model):
    _name = 'my_modulo_traduccion'
    _description = 'Modelo Traduccion'

    whatsapp = fields.Char ('Numero WhatsApp ')
    notes = fields.Text (string='notes')
