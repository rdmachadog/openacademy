# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'course'
    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    responsible = fields.Many2one('res.users')

class Session(models.Model):
    _name = 'session'
    name = fields.Char()
    instructor = fields.Many2one('res.partner')
    start_date = fields.Date()
    duration = fields.Float(help="Duration in days")
    seats = fields.Integer()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
