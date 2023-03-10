
{
    #Informe general del moduelo en la pantalla web.
    'name' : 'formulario',
    'version' : '1.0',
    'summary': 'es un aplicacion  web que tiene un formulario de informacion.',
    'sequence': 7,
    'description': """Este modulo es el cuarto modulo formulario.""",
    'category': 'extra',
    'website': 'www.myformulario.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'formulario_views.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
