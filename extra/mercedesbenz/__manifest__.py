
{
    #Informe general del moduelo en la pantalla web.
    'name' : 'mercedes benz',
    'version' : '1.0',
    'summary': 'es un aplicativo web para los clientes premium de mercedes benz',
    'sequence': 6,
    'description': """Este modulo es el septimo modulo formulario.""",
    'category': 'extra',
    'website': 'www.mercedesbenz.premium.com.co',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'mercedes_views.xml',
        'reservacion_views.xml',
        'colormercedes_views.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
