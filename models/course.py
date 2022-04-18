# -* coding: UTF-8 -*-

from odoo import models, fields, api

class Course(models.Model):

    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(String='Descritpion')

    level = fields.Selection(string='Level',
                             selection=[('beginner', 'Beginner)'
                                         'intermediate', 'Intermediate'),
                                        ('advanced', 'Advanced')],
                             copy= False)
    activate = fields.Boolean(string='Activate', default=True)


