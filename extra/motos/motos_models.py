from odoo import api, models, fields

#Estamos definiendo los campos.
class MotosModels(models.Model):
    _name = 'motos_models'
    #Esta descripcion es solo para este modelo.
    _description = 'Esta es la descripcion del kilometraje'
    nombre_moto = fields.Char( string = 'nombre de la motocicleta')
    numero_rueda = fields.Integer(string = 'numero de la rueda')
    numero_chacis = fields.Integer(string = 'numero identificacion chacis')
    #marca = fields.Selection([('honda', 'Honda'),('yamaha', 'Yamaha'),('susuki', 'susuki')], string='marca')
    marcas_ids = fields.Many2one('model_marcas', string='marcas')

    class ModelMarcas(models.Model):
        _name = 'model_marcas'
        _description = 'marcas de moto'#Puedo colocar cualquier cosa
        name = fields.Char(string='Digite marca de moto')


        
    