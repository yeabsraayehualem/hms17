# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Yoraki (Yeab A.)",
    'website': "https://www.yoraki.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital MS',
    'version': '0.1',

    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        "views/hr_employee.xml",
        "views/product.xml",
        "views/patient_card.xml",
        "views/lab_test.xml",
        "views/mri.xml",
        


        "views/menu.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'hms/static/img/patient.png',
            'hms/static/img/laboratory.png',
            'hms/static/img/mri.png',
        ],
        
    },
    'installable': True,
    'auto_install': True,
    'application': True
}

