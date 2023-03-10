from odoo import api, models, fields

#Estamos definiendo los campos.
class formularioModels(models.Model):
    _name = 'formulario_models'
    #Esta descripcion es solo para este modelo.
    _description = 'formulario_models'
    nombre = fields.Char( string = 'Digite Nombre')
    apellido = fields.Char(string = 'Digite Apellido')
    identificacion = fields.Integer(string = 'numero de identificacion')
    observaciones = fields.Char(string = 'Obersevaciones')
    departamento_id = fields.Many2one('formulario_departamento', string='Departamento')
    municipio_id = fields.Many2one('formulario_municipio', string='Municipio')
    nom_pais = fields.Many2one('nombre_pais',string='pais')

    
class Departamento(models.Model):
        _name = 'formulario_departamento'
        _description = 'Estos son los departamentos para el modelo'
        _rec_name = 'nombre_departamento'
        nombre_departamento = fields.Char(string='Departamento')
        nom_pais = fields.Many2one('nombre_pais',string='pais')     



class Municipio(models.Model):
        _name = 'formulario_municipio'
        _description = 'Estos son los municipios para el modelo'
        _rec_name = 'nombre_municipio'
        nombre_municipio = fields.Char(string='Municipio')
        departamento_id = fields.Many2one('formulario_departamento', string='Departamento')


class Pais(models.Model):
        _name = 'nombre_pais'
        _description = 'Estos son los paises para el modelo'
        _rec_name = 'nom_pais'
        nom_pais = fields.Char(string='pais')
        nom_pais = fields.Many2one('nombre_pais',string='pais') 
      
       






        