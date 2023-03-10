
{
    #Informe general del moduelo en la pantalla web.
    'name' : 'colegio',
    'version' : '1.0',
    'summary': 'es un aplicativo web para un colegio',
    'sequence': 6,
    'description': """Este modulo es el sexto modulo formulario.""",
    'category': 'extra',
    'website': 'www.myappcolegio.com',
    'author': 'johan sdg',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'colegio_views.xml','profesores_views.xml', 'materia_views.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
