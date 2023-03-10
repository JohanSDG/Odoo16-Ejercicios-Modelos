{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Tarea Productos Venta',
    'version' : '1.0',
    'summary': 'es un aplicacion  web que te enseña a heredar en odoo16 .',
    'sequence': 1,
    'description': """Este modulo es de ejemplo.""",
    'category': 'extra',
    'website': 'www.herenciamodulo.com',
    'author': 'johan sdg',
    'depends' : ['base','product'],
    'data': [
         'views/precio_venta_template_views.xml',
        ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
