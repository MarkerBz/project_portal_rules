# -*- coding: utf-8 -*-

from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"
    
    privacy_visibility_by_portal_clients = fields.Boolean(string='Privacy - By portal clients')
