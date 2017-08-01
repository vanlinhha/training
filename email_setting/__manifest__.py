# -*- coding: utf-8 -*-
{
    'name': "email_setting",

    'summary': """
        Setting up email server without turn on debug mode""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fetchmail'],

    # always loaded
    'data': [
        'views/email_view.xml',
        'security/views.xml',
        'security/ir.model.access.csv'
    ],
    'application':True,

}