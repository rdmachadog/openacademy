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
    state = fields.Selection([
                              ('draft','Draft'),
                              ('confirmed','Confirmed'),
                              ('done','Done'),
                             ], default='draft', readonly=True)
    @api.one
    def action_draft(self):
        self.state = 'draft'

    @api.one
    def action_confirm(self):
        self.state = 'confirmed'

    @api.one
    def action_done(self):
        self.state = 'done'


class Session(models.Model):
    _name = 'session'
    name = fields.Char()
    instructor = fields.Many2one('res.partner', domain=[("instructor","=",True)])
    course = fields.Many2one('course')
    start_date = fields.Date()
    duration = fields.Float(help="Duration in days")
    seats = fields.Integer()
    attendees = fields.Many2many('res.partner')
#     value = fields.Integer()
    percentage_seats_taken = fields.Float(compute="_compute_percentage_seats_taken", store='True')

    @api.depends('attendees','seats')
    def _compute_percentage_seats_taken(self):
        for record in self:
            if record.seats:
                record.percentage_seats_taken = float(len(record.attendees))/record.seats * 100.00
            else:
                record.percentage_seats_taken = 0.00

    @api.onchange('seats','attendees')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendees):
            return {
                'warning': {
                    'title': "Too mane attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }
