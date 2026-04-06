{
    'name': 'Campus Club Event Manager',
    'version': '1.0',
    'category': 'Education',
    'author': 'Campus ERP',
    'description': 'Complete mini-ERP for managing student clubs, events, budgets, sponsors, and purchase requests.',
    'depends': ['base', 'mail'],
    'data': [
        'views/campus_menus.xml',              # group and menus first
        'security/ir.model.access.csv',        # then access rights
        'data/ir_sequence.xml',
        'views/campus_club_views.xml',
        'views/campus_event_views.xml',
        'views/campus_purchase_request_views.xml',
        'views/campus_sponsor_views.xml',
        'views/campus_reporting_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
