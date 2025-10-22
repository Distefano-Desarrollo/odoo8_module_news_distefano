{
    'name': 'Modulo de Noticias',
    'version': '1.0',
    'author': 'ingekids_distefano',
    'website': '',
    'category': 'Human Resources',
    'summary': 'Modulo para gestionar noticias internas de la empresa',
    'depends': ['base', 'hr','web'],
    'data':[
        'views/actions.xml',
        'views/menu.xml',
        'views/type/tree.xml',
        'views/type/form.xml',
        'views/new/tree.xml',
        'views/new/form.xml',
        'views/new/calendar.xml',
    ],
    'installable': True,
    'auto_install': False,
    
}