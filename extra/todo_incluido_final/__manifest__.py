{
    #Informe general del moduelo en la pantalla web.
    'name' : 'Aprendizaje Diego 45 Dias',
    'version' : '1.0',
    'summary': 'es un aplicacion  web que te enseña Todos lo que haz aprendido en estos 45 dias.',
    'sequence': 1,
    'description': """Este modulo es de ejemplo.""",
    'category': 'extra',
    'website': 'wwww.avalosincore.com',
    'author': 'johan sdg',
    'depends' : ['base','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_incluido_views.xml',
        #'views/Product.xml',
        'views/pais_views.xml',
        'views/municipio_views.xml',
        'views/departamento_views.xml',
        ],
     'icon':'todo_incluido_final\static\src\img\icon.png',
        
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
