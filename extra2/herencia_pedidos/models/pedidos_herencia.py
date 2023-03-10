from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'sale.order'
    
    whatsapp = fields.Char ('Numero WhatsApp ')
    notes = fields.Text (string='notes')
    sugerencia = fields.Char('Especificacion del producto')
