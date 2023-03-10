from odoo import api, models, fields
from datetime import datetime


#Estamos definiendo los campos.
class MercedesModels(models.Model):
    _name = 'concesionario_mercedes_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Formulario para concesionario mercedes'
    nombre = fields.Char( string = 'Digite Nombre')
    apellido = fields.Char(string = 'Digite Apellido')
    genero = fields.Selection([ ('hombre', 'Hombre'),('mujer', 'Mujer')], string='Seleccione su genero')
    fecha_nacimiento = fields.Date(string = 'Digite Fecha Nacimiento')
    email = fields.Char(string = 'Digite Su Correo Electronico')
    mercedes_reservacion = fields.Many2many('reservacion_mercedes_models',string = 'El tipo de carro Que Ha Deseado')




class ReservacionModels(models.Model):
    _name = 'reservacion_mercedes_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Formulario para concesionario mercedes'
    _rec_name = 'nombre_vehiculo'
    nombre_vehiculo = fields.Char( string = 'Nombre del vehiculo de sus sueños')
    colorvehiculo = fields.Many2one('color_mercedes_models',string = ' Color de su vehiculo Mercedes')
    fecha_reservacion = fields.Date( string = 'Digite la fecha de entrega del vehiculo')
    descripcion = fields.Text( string = 'Digite la descripcion del vehiculo')



class ColorModels(models.Model):
    _name = 'color_mercedes_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Formulario para concesionario mercedes'
    _rec_name = 'color_vehiculo'
    color_vehiculo = fields.Char( string = '¿Elija El Color De Su Preferencia')
    color_interior = fields.Char( string = '¿Elija El Color Interior De Su Preferencia')
    descripcion = fields.Text( string = 'Digite la descripcion del color')

    
    

    
    
       






        