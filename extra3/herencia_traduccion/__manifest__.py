{
    #Informe general del moduelo en la pantalla web.
    'name' : ' Modulo Traduccion',
    'version' : '1.0',
    'summary': 'es un aplicacion  web que te enseña a traduccion en odoo16 .',
    'sequence': 1,
    'description': """Este modulo es de ejemplo.""",
    'category': 'extra',
    'website': 'www.herenciamodulo.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
         'views/view_traduccion.xml',
        ],
    'icon':'herencia_traduccion\static\src\img\icon.png',

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}