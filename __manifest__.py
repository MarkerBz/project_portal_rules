# -*- coding: utf-8 -*-
{
    'name': 'Project - Extended portal rules',
    'version': '10.0.1.0.0',
    'author': 'Contractor Andrey S. 2017',
    'category': 'Project',
    'description': """
Project - Extended portal rules
===============================
Project - Extended portal rules
    """,
    'depends': [
        'base',
        'project',
        'project_issue',
        'portal',
        'website_portal',
    ],
    'data': [
        'security/project_portal_rules_security.xml',
        'views/project_project_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
