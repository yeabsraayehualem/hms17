from odoo import models,fields,api     


class Product(models.Model):
    _inherit= 'product.template'

    min_threshold = fields.Float(default=0.0, string="Minimum threshold")
    max_threshold = fields.Float(default=0.0, string="Maximum threshold")
    product_type = fields.Selection([
        ('medicine', 'Medicine'),
        ('lab_test', 'Lab Test'),
        ('mri_test', 'MRI Test'),
        ('surgery', 'Surgery'),
        ('consultation', 'Consultation'),
        ('imaging', 'Imaging'),
        ('routine_checkup', 'Routine Checkup'),
       ], string="Medical Information")
    is_medical = fields.Boolean(string="Is Medical", default=False)
    