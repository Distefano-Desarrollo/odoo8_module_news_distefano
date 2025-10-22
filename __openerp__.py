{
    'name': 'Modulo de Noticias',
    'version': '1.0',
    'author': 'ingekids_distefano',
    'website': '',
    'category': 'Human Resources',
    'summary': 'Modulo para gestionar noticias internas de la empresa',
    'depends': ['base', 'hr','web'],
    'data':[
        'views/type/typeForm.xml',
        'views/type/treeType.xml',
        'views/news/newsForm.xml',
        'views/news/treeNews.xml',
        'views/news/calendarNews.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    
}