from odoo import api, models, fields

#Estamos definiendo los campos.
class PetsModels(models.Model):
    _name = 'pets_models'
    #Esta descripcion es solo para este modelo.
    _description = 'modelo mascotas'
    nombre = fields.Char( string = 'nombre mascota')
    especie = fields.Char(string = 'especie')
    apodo = fields.Char(string = 'apodo')
    
    