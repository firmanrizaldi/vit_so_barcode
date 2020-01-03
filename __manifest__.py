# -*- coding: utf-8 -*-
{
    'name': "Display Barcode on SO Report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        * Display barcode on PDF report of SO.
        * Addons ini adalah bahan praktek pada traning "Odoo QWeb Programming" yang
        diselenggarakan di vitraining.com dan E-Book "Panduang Lengkap Pemrograman
        QWeb Odoo v10"
    """,

    
    'author': 'firmanrizaldiyusup@gmail.com',
    'website': 'http://www.vitraining.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [

        'report/so.xml',
    ],
  
}