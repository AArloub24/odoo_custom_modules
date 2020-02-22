# -*- coding: utf-8 -*-
{
    'name': 'School',
    'version': '12.0.1.0.0',
    'summary': 'Record School Information',
    'category': 'Tools',
    'author': 'Arlou Beloria',
    'maintainer': '-',
    'company': '-',
    'website': 'https://www.cybrosys.com',
    'depends': ['mail', 'web', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/subject_view.xml',
    ],
    'image: [static/description/icon.png]'
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
