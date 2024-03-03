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

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
    @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        response = super(WebsiteSaleInherit, self).cart(access_token=None, revive='', **post)
        message = request.env['ir.config_parameter'].sudo().get_param('website_sale.message')
        min_order_amount = float(request.env['ir.config_parameter'].sudo().get_param('website_sale.min_order_amount'))
        is_tax_exclude = request.env['ir.config_parameter'].sudo().get_param('website_sale.is_tax_exclude')
        order = request.website.sale_get_order()
        if is_tax_exclude:
            response.qcontext['is_minimum_amount'] = True if order.amount_untaxed < min_order_amount else False
        else:
            response.qcontext['is_minimum_amount'] = True if order.amount_total < min_order_amount else False
        response.qcontext['message'] = message
        return response

    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        response = super(WebsiteSaleInherit, self).checkout(**post)
        order = request.website.sale_get_order()
        message = request.env['ir.config_parameter'].sudo().get_param('website_sale.message')
        min_order_amount = float(request.env['ir.config_parameter'].sudo().get_param('website_sale.min_order_amount'))
        is_tax_exclude = request.env['ir.config_parameter'].sudo().get_param('website_sale.is_tax_exclude')
        values = self.checkout_values(order, **post)
        values.update({'website_sale_order': order})
        response.qcontext['message'] = message
        if is_tax_exclude:
            response.qcontext['is_minimum_amount'] = True if order.amount_untaxed < min_order_amount else False
        elif not is_tax_exclude:
            response.qcontext['is_minimum_amount'] = True if order.amount_total < min_order_amount else False
        if response.qcontext['is_minimum_amount']:
            return request.redirect('/shop/cart')
        return response
