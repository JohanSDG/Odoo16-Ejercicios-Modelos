{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Tarea cliente en Partner',
    'version' : '1.0',
    'summary': 'es un aplicacion  web que te enseña a heredar en odoo16 .',
    'sequence': 1,
    'description': """Este modulo es de ejemplo.""",
    'category': 'extra',
    'website': 'www.herenciamodulo.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
         'views/cliente_res_partner_views.xml',
        ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
