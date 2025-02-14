{
    'name': "Cicles Formatius ",
    'summary': "Gestió dels cicles formatius",
    'description': """
        Gestionar els cicles formatius i mòduls .
    """,
    'author': "",
    'website': "",
    'category': 'Custom',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/cicle_formatiu_views.xml',
        'views/modul_views.xml',
        'views/alumne_views.xml',
        'views/professor_views.xml',
    ],
    'installable': True,
    'application': True,
}
