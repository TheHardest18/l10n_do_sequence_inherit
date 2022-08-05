# -*- coding: utf-8 -*-
{
    'name': "sale_order_multiply",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Isias Mateo: Isias1626@gmail.com",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '13.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/mail_template_view.xml',
        'views/mail_template_sale_view.xml',
    ],
}
