{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Edad y Fecha Herencia Cliente',
    'version' : '1.0',
    'summary': 'es un aplicacion  web que te enseña a heredar en odoo16 .',
    'sequence': 1,
    'description': """Este modulo es de ejemplo.""",
    'category': 'extra',
    'website': 'www.herenciamodulo.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
         'views/view_fecha.xml',
        ],
    'icon': 'herencia_clientes_fecha_edad\static\src\img\edad.jpg',

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}