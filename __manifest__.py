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

{
    'name': 'Minimum Order Amount | Restrict Orders',
    'version': '17.0.1.0.0',
    'summary': """The Minimum Order Amount App for odoo empowers your e-commerce business with the ability
    to set minimum order requirement to complete a purchase. Encourage customers to enhance their shopping
    experience by adding more item to their cart, ultimately increasing your average order value and revenue.""",
    'description': """Setting a minimum order amount in odoo implies that your customers must add items to their 
    shopping carts and reach a certain order value in order to continue with the checkout process. 
    If you sell cheaper things in your store, the shipping expense could occasionally exceed the cost of the 
    merchandise. Of course, you can send these orders, but in an effort to avoid them, you frequently need to 
    provide a minimum order quantity. The checkout page will show an error message if the customer's shopping cart 
    contains items with a total value below the minimum order amount. The client must place a minimum order amount 
    before the purchase may be completed.""",
    'category': 'eCommerce',
    'author': 'Weblytic Labs',
    'company': 'Weblytic Labs',
    'website': "https://store.weblyticlabs.com",
    'depends': ['base', 'website', 'website_sale', 'mail', 'account'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
