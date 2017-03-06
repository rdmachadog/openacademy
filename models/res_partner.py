# -*- coding: utf-8 -*-

from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'


    instructor = fields.Boolean(help="This partner give training in our courses")
