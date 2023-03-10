from odoo import models, fields, api
from datetime import date

class Products(models.Model):
    _name = 'products_booking'
    _description = 'products_booking'
    
    usuario_id = fields.Many2one('res.partner', string='Customer')  # Cliente que realiza la reserva
    product_id = fields.Many2one('product.template', string='Product')
    birth_date = fields.Date(string = 'Birth date')
    age = fields.Char(string = 'Age', compute='calculate_age')
    tipeidentification = fields.Selection([ ('cedula', 'Cedula'),('dni', 'DNI'),('pasaporte', 'Identificacion Pasaporte')],string = 'select identification type')
    number_identification = fields.Integer(string = 'Numberidentification')
    Star_date = fields.Date(string='Star Date', tracking=True, required=True)  # Fecha de inicio de la reserva
    End_date = fields.Date(string='End Date', tracking=True, required=True)  # Fecha de fin de la reserva
    Reserved_days = fields.Integer(string='Dias Reservados', compute='_compute_buscar_reservas')  # Número de días reservados
    #valor_reserva = fields.Float(string='Valor Reserva', compute='_compute_valor_reserva')  # Valor de la reserva
    state = fields.Selection([('draft', 'Borrador'),('confirmed', 'Confirmado'),('done', 'Realizado'),('cancelled', 'Cancelado')], string='state', default='draft', tracking=True)#estado
    notes = fields.Text(string='notes')#notas
    country = fields.Many2one('country_form', 'Choose your country')#pais
    department = fields.Many2one('form_departament', string='Departament')#departamento
    municipality = fields.Many2one('form_municipality', string='municipality')#municipio


    # Metodos para cambiar el state de las reservas 
    def confirmar_reservacion(self):
        self.ensure_one()
        self.state = 'confirmed'

    def mark_as_done(self):
        self.ensure_one()
        self.state = 'done'
    
    def cancel_reservation(self):
        self.ensure_one()
        self.state = 'cancelled'

    def change_borrador(self):
        self.ensure_one()
        self.state = 'draft'

    # Permite verificar que el numero de dias de la reserva y que la fecha de salida no sea inferior al ingreso
    # Tambien que la reserva minima sea un dia, si la fecha de ingreso y salida es el mismo Dia
    @api.depends('Star_date', 'End_date')
    def _compute_buscar_reservas(self):
        for record in self:
            if record.Star_date and record.End_date:
                Star_date = fields.Datetime.from_string(record.Star_date)
                End_date = fields.Datetime.from_string(record.End_date)
                if Star_date == End_date:
                    record.Reserved_days = 1
                else:
                    record.Reserved_days = int((End_date - Star_date).days)
            else:
                record.Reserved_days = 1

    @api.depends('birth_date')
    def calculate_age(self):
        today = date.today()
        for record in self:
            birth_date = record.birth_date
            if birth_date:
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0


class Departamento(models.Model):
        _name = 'form_departament'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'nom_state'
        nom_state = fields.Char(string='Departamento')
    
class Municipio(models.Model):
        _name = 'form_municipality'
        _description = 'Este formulario es para los clientes premium starbucks'
        _rec_name = 'name_municipality'
        name_municipality = fields.Char(string='Municipio')
        department = fields.Many2one('formulario_departamento_starbucks', string='Departamento')

class Pais(models.Model):
        _name = 'country_form'
        _description = 'Este formulario crecimiento'
        _rec_name = 'name_country'
        name_country = fields.Char(string='country')