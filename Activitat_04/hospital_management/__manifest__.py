{
    'name': 'Hospital Management',
    'version': '1.0',
    'author': "",
    'website': "",
    'category': 'Healthcare',
    'summary': 'Gestió de pacients i metges d’un hospital',
    'description': """
    Aquest mòdul permet gestionar pacients, metges i les atencions realitzades.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}

