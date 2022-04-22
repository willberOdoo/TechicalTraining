# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',

    'summary': """Academy app to manage Training""",

    'description': """ 
        Academy Module ti manage Training:
        -Courses
        -Sessions
        -Attendees
    """,
    'autor': 'Payall',

    'developer': 'Willber R.R',
    
    'website': 'htps://www.odoo.com',

    'category': 'Training',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',

    ],

    'demo': [
        'demo/academy_demo.xml',
    ],
}