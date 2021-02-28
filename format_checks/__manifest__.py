# -*- coding: utf-8 -*-
{
    'name': "format_checks",

    'summary': """
        Modification to checks layout""",

    'description': """
        Modification to checks layout
    """,

    'author': "Avalantec",
    'website': "https://www.avalantec.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'account_accountant',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','l10n_us_check_printing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'Report/report_check_top.xml',
        'views/views.xml',
    ],

}