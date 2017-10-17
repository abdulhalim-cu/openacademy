# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage Training""",

    'description': """Open Academy module for training:
                        - training courses
                        - training sessions
                        - attendees registration
                    """,

    'author': "Abdul Halim",
    'website': "http://aristobd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    'application':True,
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
