# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
       Module for Managing Hospital """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Arlou Beloria",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/create_appointment.xml',
        'wizards/create_specialization.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/specialization.xml',
        'data/sequence.xml',
        'reports/patient_card.xml',
        'reports/report.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
