# -*- coding: utf-8 -*-

{
    'name': 'BlueSnap Payment Acquirer',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: BlueSnap Implementation',
    'version': '9.0.0.0.0',
    'description': """BlueSnap Payment Acquirer""",
    'author': 'Moldeo Interactive - www.moldeo.coop',
    'depends': ['payment'],
    'data': [
        'views/bluesnap.xml',
        'views/payment_acquirer.xml',
        'views/res_config_view.xml',
        'data/bluesnap.xml',
    ],
    'test': [
    ],
    'installable': True,
}
