# -*- coding: utf-8 -*-

##############################################################################
#
#    Weblytic Labs.
#    Copyright (C) 2023 Weblytic Labs (<https://weblyticlabs.com>).
#    Author: WeblyticLabs <support@weblyticlabs.com>
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    min_order_amount = fields.Float(string="Minimum Order Amount")
    is_tax_exclude = fields.Boolean(string="Tax Excluded", default=True)
    message = fields.Text(string="Message")

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('website_sale.min_order_amount', self.min_order_amount)
        self.env['ir.config_parameter'].sudo().set_param('website_sale.is_tax_exclude', self.is_tax_exclude)
        self.env['ir.config_parameter'].sudo().set_param('website_sale.message', self.message)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ir_config_parameter_sudo = self.env['ir.config_parameter'].sudo()
        res.update(
            min_order_amount=ir_config_parameter_sudo.get_param('website_sale.min_order_amount'),
            is_tax_exclude=ir_config_parameter_sudo.get_param('website_sale.is_tax_exclude'),
            message=ir_config_parameter_sudo.get_param('website_sale.message'),
        )
        return res
