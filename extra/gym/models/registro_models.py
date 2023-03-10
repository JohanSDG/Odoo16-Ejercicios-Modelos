from odoo import api, models, fields

class Registro(models.Model):
        _name = 'registro_models'
        _description = 'Este formulario es para los clientes premium starGym'
        #_rec_name = 'nombre_usuario'
        nombre_usuario = fields.Char(string='Nombre')
        apellido_usuario = fields.Char(string='Apellido')
        ingreso_date = fields.Date(string='fecha ingreso', tracking=True, required=True)  # Fecha de inicio de la reserva
        salida_date = fields.Date(string='fecha salida', tracking=True, required=True)  # Fecha de fin de la reserva
        days_booked = fields.Integer(string='Dias', compute='_compute_calculo_dias', store=True)  # Número de días reservados
        #plan_usuario = fields.Selection([ ('black', 'Plan black = 85.000'),('white', 'Plan white = 75.000'),('blue', 'Plan blue = 65.000')],string = 'seleccione Plan ')
        #precio_producto = fields.Integer(string='Digite el precio de tu plan', required=True)
        #valor_total = fields.float(string='valor total', compute='_compute_valor_total', store=True)
        #product_id = fields.Many2one(string='Product', tracking=True, required=True)
        

        @api.depends('ingreso_date', 'salida_date')
        def _compute_calculo_dias (self):
                for record in self:
                    if record.ingreso_date and record.salida_date:
                        ingreso_date = fields.Datetime.from_string(record.ingreso_date)
                        salida_date = fields.Datetime.from_string(record.salida_date)
                        if ingreso_date == salida_date:
                            record.days_booked = 1
                        else:
                            record.days_booked = int((salida_date - ingreso_date).days)
                    else:
                        record.days_booked = 1


        # @api.depends('precio_producto', 'days_booked')
        # def _compute_valor_total(self):
        #         for record in self:
        #             record.valor_total = record.precio_producto * record.days_booked
        

    