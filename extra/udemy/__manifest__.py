{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Udemy',
    'version' : '1.0',
    'summary': 'es un aplicacion  web que te enseña a heredar en odoo16 .',
    'sequence': 1,
    'description': """Este modulo es de ejemplo.""",
    'category': 'extra',
    'website': 'www.cursoudemy.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/udemy_ejemplo_views.xml',
        ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
