from odoo import models, fields, api

class LabTest(models.Model):
    _name = 'patient.lab.test'

    name=fields.Char(string="Reference", default="New")
    card_id = fields.Many2one('patient.card', string='Patient Card')
    test_name = fields.Many2one('product.template',string='Test Name', domain=[('detailed_type', '=', 'service')])
    result = fields.Char(string='Result')
    min_threshold = fields.Float(string='Minimum Threshold', related="test_name.min_threshold")
    max_threshold = fields.Float(string='Maximum Threshold', related="test_name.max_threshold")
    status = fields.Integer(string='Status',default=0)
    color = fields.Char(string='Color',default="white")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('lab.test.sequence') or 'New'
        return super(LabTest, self).create(vals)