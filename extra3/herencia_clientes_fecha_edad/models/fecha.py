from odoo import models, fields, api
from datetime import date

class ResPartner(models.Model):
    _inherit = 'res.partner'
    #_description = 'Edad del usuario por medio de la fecha'

    fecha_nacimiento = fields.Date('Fecha de nacimiento', required=True)
    edad = fields.Integer('Edad', compute='_compute_edad', store=True)

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        today = date.today()
        for record in self:
            fecha_nacimiento = record.fecha_nacimiento
            if fecha_nacimiento:
                edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
                record.edad = edad
            else:
                record.edad = 0
