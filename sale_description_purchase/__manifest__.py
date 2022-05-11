# -*- coding: utf-8 -*-
{
    'name': "sale_description_purchase",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "isias1626@gmail.com",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '14.0.0.0.1',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
