from odoo import api, models, fields

#Estamos definiendo los campos.
class AvionesModels(models.Model):
    _name = 'aviones_models'
    #Esta descripcion es solo para este modelo.
    _description = 'descipcion del avion'
    nombreavion = fields.Char( string = 'nombre del avion')
    modeloavion = fields.Char(string = 'modelo del avion')
    numeroavion = fields.Integer(string = 'numero de identificacion')
    
    