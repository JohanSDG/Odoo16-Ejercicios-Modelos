from odoo import api, models, fields
from datetime import datetime


#Estamos definiendo los campos.
class EstudiantesModels(models.Model):
    _name = 'formulario_colegio_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Formulario de orden del colegio liceo infantil y juvenil'

    nombre = fields.Char( string = 'Digite Nombre')
    apellido = fields.Char(string = 'Digite Apellido')
    genero = fields.Selection([ ('hombre', 'Hombre'),('m', 'Mujer')], string='Seleccione su genero')
    fecha_nacimiento = fields.Date(string = 'Digite Fecha Nacimiento')
    email = fields.Char(string = 'Digite Su Correo Electronico')
    materia = fields.Many2many('materias_models',string = 'Digite las materias')
    profesor = fields.Many2one('profesores_models',string = 'Seleccione Profesor')
    is_active = fields.Boolean(string = 'Activo')
    almuerzo = fields.Boolean(string = 'Almuerzo')
    edad = fields.Integer(compute='_compute_edad', store=True, string = 'Su Edad Se Definio Automaticamente')
    observaciones = fields.Char(string = 'Obersevaciones')



class MateriaModels(models.Model):
    _name = 'materias_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Formulario de orden de las materias colegio liceo infantil y juvenil'
    nombreMateria = fields.Char( string = 'Digite Nombre de la materia')
    descripcion = fields.Text( string = 'Digite la descripcion de la materia ')



class ProfesoresModels(models.Model):
    _name = 'profesores_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Formulario de orden de los profesores del colegio liceo infantil y juvenil'
    _rec_name = 'nombreProfesor'
    nombreProfesor = fields.Char( string = 'Digite nombre del profesor')
    apellidoP = fields.Char( string = 'Digite el apellido del profesor')
    fechaNacimientoP = fields.Date(string = 'Digite Fecha Nacimiento')
    telefonoP = fields.Integer( string = 'Digite telefono')
    direccionP = fields.Char( string = 'Digite su direccion')
    emailP = fields.Char( string = 'Digitar correo electronico')
    #edadP = fields.Integer( string = 'Su Edad Se Definio Automaticamente')
    

    
    
       






        