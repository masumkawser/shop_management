# -*- coding: utf-8 -*-

from odoo import models, fields, api


class shop_management(models.Model):
    _name = 'shop.management'
    _description = 'shop_management.shop_management'
    _rec_name = "product_name"
    _inherit = ["mail.thread","mail.activity.mixin"]

    product_name = fields.Char(string="Product Name")
    product_price = fields.Float(string="Price", tracking=True)
    product_note = fields.Char(string="Product Note")
    product_img = fields.Binary(string="Image")
    # reference = fields.Char(string="Reference",required=True)
    priority = fields.Selection([('0','Normal'),('1','Low'),('2','High'),('3','Very High'),('4','Very Low')],string="Priority")
    state=fields.Selection([('draft', 'Draft'),('confirm', 'Confirmed'),('done', 'Done'),('cancel', 'Cancelled')], default='draft', string="Status")
    page_note = fields.Text(string="Page Note")




    def action_confirm(self):
        self.state='confirm'

    def action_done(self):
        self.state='done'