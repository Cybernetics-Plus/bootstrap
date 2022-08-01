# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Cybernetics Plus Install Bootstrap v 5.2 in Odoo
#
###################################################################################

{
    'name': 'Bootstrap Icons',
    'version': '15.1.9.0.1',
    'summary': """ 
            Cybernetics Plus Install Bootstrap v 5.2 in Odoo
            .""",
    'description': """ 
            Cybernetics Plus Install Bootstrap v 5.2 in Odoo
            .""",
    'author': 'Cybernetics Plus Co., Ltd.',
    'website': 'https://www.cybernetics.plus',
    'live_test_url': 'https://www.cybernetics.plus',
    'images': ['static/description/banner.png'],
    'category': 'Extra Tools',
    "license": 'Other proprietary',
    'price': 1.9,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': True,
    'contributors': [
        'Developer <dev@cybernetics.plus>',
    ],
    'assets': {
        'web.assets_qweb': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_common_minimal': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_common': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_common_lazy': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_backend': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        "web.assets_backend_legacy_lazy": [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_frontend': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_frontend_minimal': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_frontend_lazy': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.assets_backend_prod_only': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.report_assets_common': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
        'web.report_assets_pdf': [
            'ctp_bootstrap/static/src/css/bootstrap.min.css',
            'ctp_bootstrap/static/src/js/bootstrap.bundle.min.js',
        ],
    },
}
