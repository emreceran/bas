# -*- coding: utf-8 -*-
{
    'name': "bas",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"hr_recruitment" , 'mail', 'website_hr_recruitment', 'hr'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/birim_views.xml',
        'views/res_user_views.xml',
        'views/signup.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/ilce_mahalle_data.xml',
        'data/stages_update.xml',
        # 'data/il_ilce_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'bas/static/src/js/signup.js',
            'bas/static/src/js/profile_edit.js',
        ],
    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
