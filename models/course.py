# -* coding: UTF-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Course(models.Model):

    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(String='Descritpion')

    level = fields.Selection(string='Level',
                             selection=[('beginner', 'Beginner'),
                                        ('intermediate', 'Intermediate'),
                                        ('advanced', 'Advanced')],
                             copy=False)
    activate = fields.Boolean(string='Activate', default=True)

    base_price = fields.Float(string='Base Price', defalt=0.000)

    additional_fee = fields.Float(string='Additional Fee', default=10.00)

    total_price = fields.Float(string='Total Price', readomly=True)

    session_ids = fields.One2many(comodel_name='academy.session',
                                  inverse_name='course_id',
                                  string='Sessions')

    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base Price cannot be set as Negative.')

        self.total_price = self.base_price + self.additional_fee

        @api.constrains('additiona_fee')
        def _check_additional_fee(self):
            for record in self:
                if record.additional_fee < 10.00:
                    raise ValueError('Additional Fees cannot be less than 10.00:'
                                     '% record.additional_fee')




