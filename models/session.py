# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Session(models.Model):
     _name = 'academy.session'
     _description =  'Session Info'

     course_id = fields.Many2one(comodel_name='academy.course',
                                string='Course',
                                required=True)

     name = fields.Char(string='Title',realated='course_id.name')

     instructor_id = fields.Many2one(comodel_name='res.partner',string='Instructor')

     student_id = fields.Many2one(comodel_name='res.partner', string='Students')




