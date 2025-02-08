from odoo import models, fields, api

class MRITest(models.Model):
    _name = "mri.test"
    _description = "MRI Test"

    name = fields.Char(string="Reference", default="New")
    card_id = fields.Many2one('patient.card', string="Card No.")
    patient_name = fields.Char(string="Test Patient Name", related="card_id.patient_id.patient_name")
    date = fields.Date(string="Test Date", default=fields.Date.context_today)
    result = fields.Binary(string="Result")
    test_type = fields.Selection([(i, i.capitalize()) for i in ['Brain', 'Spine', 'Abdomen', 'Cardiac', 'Joint']], string='Test Type')
    status = fields.Selection([(i, i.capitalize()) for i in ['pending', 'completed', 'cancelled']], string='Status', default='pending')

    # Add the mri_test_sequence field to store the sequence
    mri_test_sequence = fields.Char(string="MRI Test Sequence", readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('mri.test.sequence') or 'New'
        record = super(MRITest, self).create(vals)
        record.mri_test_sequence = record.name  # Assign the generated sequence to the field
        return record
