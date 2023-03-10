from odoo import models, fields, api
from datetime import date

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    rentabilidad = fields.Float(compute='_compute_rentabilidad', store=True)
    porcentaje_rentabilidad = fields.Float(compute='_compute_porcentaje_rentabilidad', store=True, string='% de Rentabilidad')
    socio1 = fields.Float(string="Socio Johan SDG", compute="_compute_socio1")
    socio2 = fields.Float(string="Socio Diego Avalos", compute="_compute_socio2")

    @api.depends('list_price', 'standard_price')
    def _compute_rentabilidad(self):
        for product in self:
            product.rentabilidad = product.list_price - product.standard_price


    @api.depends('rentabilidad', 'standard_price')
    def _compute_porcentaje_rentabilidad(self):
        for product in self:
            if product.standard_price > 0:
                product.porcentaje_rentabilidad = (product.rentabilidad / product.standard_price) * 100
            else:
                product.porcentaje_rentabilidad = 0

    @api.depends('rentabilidad')
    def _compute_socio1(self):
        for product in self:
            product.socio1 = product.rentabilidad / 2
    
    @api.depends('rentabilidad')
    def _compute_socio2(self):
        for product in self:
            product.socio2 = product.rentabilidad / 2
