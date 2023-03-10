
{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Starbuscks Premium',
    'version' : '1.0',
    'summary': 'es un aplicacion  web para los clientes premium starbucks.',
    'sequence': 4,
    'description': """Este modulo es el septimo modulo formulario.""",
    'category': 'extra',
    'website': 'www.premiumstarbucks.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'starbucks_views.xml',
        'departamento_views.xml',
        'municipio_views.xml',
        'pais_views.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
