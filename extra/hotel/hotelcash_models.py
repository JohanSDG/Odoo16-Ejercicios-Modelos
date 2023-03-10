from odoo import api, models, fields

#Estamos definiendo los campos.
class   HuespedModels(models.Model):
    _name = 'huespedpersonas_models'
    #Modulo Principal
    _description = 'modulo de huesped nombre,apellido,email'
    nombre = fields.Char( string = 'Nombre del huesped')
    apellido = fields.Char(string = 'Apellido del huesped')
    identificacion = fields.Integer(string = 'numero de identificacion')
    email = fields.Char(string = 'Digite Email')
    observaciones = fields.Char(string = ' Requerrimientos del Huesped')
    departamento_id = fields.Many2one('formulario_departamento', string='Departamento')
    municipio_id = fields.Many2one('formulario_municipio', string='Municipio')
    pais_id = fields.Many2one('formulario_pais', string = 'pais')
    #ingreso_persona = fields.Date('ingeso_huesped', string = 'Ingreso Huesped')
    

class Departamento(models.Model):
        _name = 'formulario_departamento'
        _description = 'Estos son los departamentos para el hotel cash'
        _rec_name = 'nombre_departamento'
        nombre_departamento = fields.Char(string='Departamento')
        


class Municipio(models.Model):
        _name = 'formulario_municipio'
        _description = 'Estos son los municipios para el modelo'
        _rec_name = 'nombre_municipio'
        nombre_municipio = fields.Char(string='Municipio')
        

class Pais(models.Model):
        _name = 'formulario_pais'
        _description = 'Estos son los paises para el modelo'
        _rec_name = 'nombre_pais'
        nombre_pais = fields.Char(string='pais')
        


class Reservacion(models.Model):
    _name = 'model_reservacion'

    #_rec_name = 'ingeso_huesped'
    ingeso_huesped = fields.Date(string='ingreso')
    salida_huesped = fields.Date(string='salida')
    dias_reservados = fields.Integer(string='dias reservados')

#     @api.depends('ingreso', 'salida')
#     def _compute_dias_reservados(self):
#         for record in self:
#             if record.ingreso and record.salida:
#                 ingreso = fields.Datetime.from_string(record.ingreso)
#                 salida = fields.Datetime.from_string(record.salida)
#                 delta = salida - ingreso
#                 record.dias_reservados = delta.dias_reservados

