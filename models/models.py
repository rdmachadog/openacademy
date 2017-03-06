# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'course'
    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    responsible = fields.Many2one('res.users')
    sessions = fields.One2many('session','course')

class Session(models.Model):
    _name = 'session'
    name = fields.Char()
    instructor = fields.Many2one('res.partner')
    course = fields.Many2one('course')
    start_date = fields.Date()
    duration = fields.Float(help="Duration in days")
    seats = fields.Integer()
    attendees = fields.Many2many('res.partner')
#     value = fields.Integer()
    percentage_seats_taken = fields.Float(compute="_compute_percentage_seats_taken")
#
    @api.multi
    def _compute_percentage_seats_taken(self):
        for record in self:
            if record.seats:
                record.percentage_seats_taken = float(len(record.attendees))/record.seats * 100.00
            else:
                record.percentage_seats_taken = 0.00

