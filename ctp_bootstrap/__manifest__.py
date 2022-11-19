# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Install Bootstrap v 5.2 in Odoo
#
###################################################################################

{
    "name": "Bootstrap",
    "version": "16.1.9.0.1",
    "summary": """ 
            Install Bootstrap v 5.2 in Odoo
            .""",
    "description": """ 
            Install Bootstrap v 5.2 in Odoo
            .""",
    "author": "Cybernetics+",
    "website": "https://www.cybernetics.plus",
    "live_test_url": "https://www.cybernetics.plus",
    "images": ["static/description/banner.gif"],
    "category": "Extra Tools",
    "license": "AGPL-3",
    "price": 4.9,
    "currency": "EUR",
    "installable": True,
    "application": True,
    "auto_install": True,
    "contributors": [
        "Developer <dev@cybernetics.plus>",
    ],
    "assets": {
        "web.assets_qweb": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_common_minimal": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_common": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_common_lazy": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_backend": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_backend_legacy_lazy": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_frontend": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_frontend_minimal": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_frontend_lazy": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.assets_backend_prod_only": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.report_assets_common": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
        "web.report_assets_pdf": [
            "ctp_bootstrap/static/src/css/bootstrap.min.css",
            "ctp_bootstrap/static/src/js/bootstrap.bundle.min.js",
        ],
    },
}
