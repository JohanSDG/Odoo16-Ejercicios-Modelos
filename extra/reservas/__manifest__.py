# -*- coding: utf-8 -*-
{
    'name': "Buscar Lugar Deseado",
    'summary': "Permite reservar dependiendo al lugar y y fecha",
    'description': """
        Permite reservar productos y buscarlo dependiendo a la fecha y lugar.
    """,

    'author': "JohanSDGCorp",
    'website': "https://www.johansdgcorp.com",
    'category': 'Productividad',
    'version': '101.8',
    'depends': ['base'],
    'application' : True,
    'sequence' : '1',
    'data': [
        'security/ir.model.access.csv',
        'views/buscar_reserva.xml',
        'views/pais.xml',
    ],
    'icon':'reserva\img\Imagen_negra_buscar2.png',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    
}
