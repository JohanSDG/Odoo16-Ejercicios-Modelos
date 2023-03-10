#from odoo import api, models, fields
from odoo import api, models, fields, tools, exceptions, _
from datetime import datetime


#Estamos definiendo los campos.
class formularioModels(models.Model):
    _name = 'stargym_usuario_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Este formulario es para los clientes premium de starGym'
    nombre = fields.Char( string = 'Name')
    apellido = fields.Char(string = 'Last Name')
    fecha_nacimiento = fields.Date(string = 'Birth date')
    #edad = fields.Integer(string = 'Edad',compute='_compute_edad')
    ciudad = fields.Char(string = 'City')
    departamento_id = fields.Many2one('formulario_departamento_stargym', string='State')
    municipio_id = fields.Many2one('formulario_municipio_stargym', string='Municipality')
    pais_id = fields.Many2one('formulario_pais_stargym',string='Country')
    email = fields.Char(string = 'Email')
    referido = fields.Many2one('referidos_models',string='Referrals')
    tipoidentificacion = fields.Selection([ ('cedula', 'Cedula'),('dni', 'DNI'),('pasaporte', 'Identificacion Pasaporte')],string = 'seleccione Tipo Identificacion')
    numero_identificacion = fields.Integer(string = 'number identification')
    genero = fields.Selection([ ('hombre', 'Men'),('mujer', 'Women')], string='Seleccione su genero')
    peso = fields.Float(string = 'Enter your weight')
    discapacidad = fields.Boolean(string = 'Do you have discapacibility')
    horarios_entrenamiento = fields.Selection([ ('Manana', 'Mañana'),('mediodia', 'Medio Dia'),('tarde', 'Tarde'),('noche', 'Noche')],string = 'Seleccione Horario')
    estado = fields.Selection([('new', 'nuevo'),('confirmed', 'Confirmado'),('inactive', 'Inactivo')], string='Estado', default='new', tracking=True)
    entrenador = fields.Many2one('entrenador_modulos',string= 'Seleccione Entrenador/a')
    
    # @api.depends('fecha_nacimiento')
    # def _compute_edad(self):
    #     for record in self:
    #         if record.fecha_nacimiento:
    #             hoy = fields.Date.today()
    #             edad = hoy.year - record.fecha_nacimiento.year - ((hoy.month, hoy.day) < (record.fecha_nacimiento.month, record.fecha_nacimiento.day))
    #             record.edad = edad

# Metodos para cambiar el estado de las reservas y asignarla en el xml
    def confirmar_entrada(self):
        self.ensure_one()
        self.state = 'confirmed'

    def mark_as_done(self):
        self.ensure_one()
        self.state = 'inactive'

    def change_borrador(self):
        self.ensure_one()
        self.state = 'new'












        
       






        