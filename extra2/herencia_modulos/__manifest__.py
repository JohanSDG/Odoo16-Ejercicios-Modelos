# -*- coding: utf-8 -*-
{
    'name': "Reservacion Productos",
    'summary': "Permite reservar productos ",
    'description': """
        Permite reservar productos
        Permite establecer reservas con datos del cliente, producto reservado,
         fecha de inicio de reserva, fecha final, calcular automaticamente el numero de dias reservados, 
         el valor de la reserva, validar fechas de inicio y final.
    """,

    'author': "JohanSDGCompany",
    'website': "https://www.johansdgcompany.com",
    'category': 'Productividad',
    'version': '101.8',
    'depends': ['base','product', 'mail'],
    'application' : True,
    'sequence' : '1',
    'data': [
        'security/ir.model.access.csv',
        'views/views_general.xml',
        'views/product_views.xml',
        'views/website_views.xml',
        'data/sequence.xml',
        'views/snippets/products_booking_snippets.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    
    'assets': {
        'website.assets_backend': [],
        'web.assets_frontend': [
            'products_booking/static/src/css/products_booking_styles.css',
        ],
    },
    'icon': 'herencia_modulos\static\src\img\Reservaciones.png',
}