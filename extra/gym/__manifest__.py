
{
    #Informe general del moduelo en la pantalla web.
    'name' : 'StarGym Premium',
    'version' : '1.0',
    'summary': 'es un aplicacion  web para los clientes premium starGym .',
    'sequence': 1,
    'description': """Este modulo es el decimo modulo.""",
    'category': 'extra',
    'website': 'www.premiumstargym.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/stargym_usuario_views.xml',
        'views/departamento_views.xml',
        'views/municipio_views.xml',
        'views/pais_views.xml',
        'views/entrenador_views.xml',
        'views/registro.xml',
        'views/referidos.views.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
