# -*- coding: utf-8 -*-

from csv import Dialect
from email.policy import default
from re import S
from tkinter import dialog
from unittest import result
from odoo import api, models, fields, tools, exceptions, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero
from odoo.addons import bus


class ProductProduct(models.Model):
    _inherit = 'product.template'
    can_be_booked = fields.Boolean(string='Can be Booked', default=True)
    reservation_ids = fields.One2many('products_booking', 'product_id', string='Reservations')
    website_description_booking = fields.Html('Descripcion Booking')

    def action_view_reservations(self):
        action = self.env["ir.actions.actions"]._for_xml_id("products_booking.action_view_reservations")
        action['domain'] = [('product_id', '=', self.id)]
        action['display_name'] = _("Reservations for %s", self.display_name)
        return action