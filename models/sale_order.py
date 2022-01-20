from odoo import api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_test_sh(self):
        raise UserError('Hello Odoo SH')
