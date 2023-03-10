
{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Hospital Central Javeriano',
    'version' : '1.0',
    'summary': 'es un aplicacion  web para los clientes y su agendamiento de citas',
    'sequence': 3,
    'description': """Este modulo es el octavo formulario.""",
    'category': 'extra',
    'website': 'www.clinicacentraljaverian.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'hospital_central_javeriano.views.xml',
        'departamento_views.xml',
        'municipio_views.xml',
        'pais_views.xml',
        'doctor_views.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
