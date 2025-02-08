from odoo import models,fields,api     


class Product(models.Model):
    _inherit= 'product.template'

    min_threshold = fields.Float(default=0.0, string="Minimum threshold")
    max_threshold = fields.Float(default=0.0, string="Maximum threshold")