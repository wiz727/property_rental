import re

from odoo import models, fields, api
import math


class PosOrder(models.Model):
    _inherit = 'pos.order'

    pos_config = fields.Many2many('pos.config', 'pos_receipt')

    @api.constrains('pos_config')
    def test(self):
        for record in self:
            print(record.pos_config)
            for rec in record.pos_config:
                print(rec)
    @api.model
    def get_custom_data(self, id):
        pos_order_id = self.search([('id', '=', id)])

        return {
            'order_id': pos_order_id.id,
            'order_name': pos_order_id.name,
        }
