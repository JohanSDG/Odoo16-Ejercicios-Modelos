# -*- coding: utf-8 -*-
from odoo import http
from odoo.modules.module import OdooHook
from odoo.http import request

# Ejemplo de agregar texto directamente al la pagina
class ProductsBooking(http.Controller):
    @http.route('/products_booking', auth='public')
    def index(self, **kw):
        return "Hello, world"



#Trabajando con rutas y redirecciones
class CustomContact(http.Controller):

    # Redirigir una pagina ruta a otra
    @http.route('/contactus', auth='public', website='True')
    def contactus_redireccion(self):
        return request.redirect('/contacto')

    # Renderizar una plantilla
    @http.route('/contacto', auth='public', website='True')
    def contacto_render(self):
        return http.request.render('website.contactus', {})


# Cambiar la ruta del login
class CustomLogin(http.Controller):
    
    # Una nueva ruta para acceder al login
    @http.route('/login', auth='public', website='True')
    def login_redireccion(self):
        return http.request.render('web.login', {})

# Controlador de snippet de busqueda

class ProductController(http.Controller):
    @http.route(['/shop/<string:search>'], type='http', auth="public", website=True)
    def search(self, search='', **post):
        products = request.env['product.template'].search([('name', 'ilike', search)])
        return request.render("website_sale.products", {'products': products})
