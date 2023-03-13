# -*- coding: utf-8 -*-
{
    'name': "Coworking Hotel",
    'summary': "Permite reservar",
    'description': """
        Permite reservar productos
        Permite establecer reservas con datos del cliente, producto reservado,
         fecha de inicio de reserva, fecha final, calcular automaticamente el numero de dias reservados, 
         el valor de la reserva, validar fechas de inicio y final.
    """,

    'author': "JohanSDGCorp",
    'website': "https://www.johansdgcorp.com",
    'category': 'Productividad',
    'version': '101.8',
    'depends': ['base','product'],
    'application' : True,
    'sequence' : '1',
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'icon': 'coworking/static/src/img/icon.png',
}