# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ShopManagement(http.Controller):
    @http.route('/shop', type='http', auth="public", website=True)
    def product_list(self, **kw):
        shops = request.env['shop.management'].sudo().search([])
        return request.render('shop_management.template_shop_web', {'shops': shops})