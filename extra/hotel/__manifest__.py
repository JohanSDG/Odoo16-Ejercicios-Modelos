
{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Hotel',
    'version' : '1.0',
    'summary': 'es un aplicacion  web para el hotelcash.',
    'sequence': 6,
    'description': """Este modulo es el septimo modulo formulario.""",
    'category': 'extra',
    'website': 'www.myhotelcash.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'hotelcash_views.xml','departamento_views.xml','municipio_views.xml','pais_views.xml','reservacion_views.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
