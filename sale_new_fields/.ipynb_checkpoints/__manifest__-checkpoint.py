# -*- coding: utf-8 -*-
{
    'name': "sale_new_fields",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Isias Mateo: Isias1626@gmail.com",
    'website': "github.com/thehardest18",
    'category': 'Uncategorized',
    'version': '15.0.0.0.1',
    'depends': ['base','sale_management', 'mrp'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
