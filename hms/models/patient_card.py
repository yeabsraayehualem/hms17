from odoo import models, fields, api
from datetime import datetime

class PatientCard(models.Model):
    _name = 'patient.card'
    _description = 'Patient Card'
    _order = 'name desc'  # Sort by latest record

    name = fields.Char(string="Card Number", required=True, copy=False, readonly=True, default="New")
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_name = fields.Char(related='patient_id.name', string='Patient Name', readonly=True)
    age = fields.Integer(related='patient_id.age', string='Age', readonly=True)
    gender = fields.Selection(related='patient_id.gender', string='Gender', readonly=True)
    date_of_birth = fields.Date(related='patient_id.date_of_birth', string='Date of Birth', readonly=True)
    address = fields.Text(related='patient_id.address', string='Address', readonly=True)
    phone_number = fields.Char(related='patient_id.phone_number', string='Phone Number', readonly=True)
    date = fields.Date(string="Date", default=fields.Date.context_today, readonly=True)
    lab_test= fields.One2many('patient.lab.test','card_id')
    mri_test = fields.One2many('mri.test', 'card_id')
    total_price = fields.Float(string="Total Price", default=0.0, compute="_total_price_computation")
    is_paid = fields.Boolean(compute='_is_paid_computation', string="Is Paid?", default=False)
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.card') or 'New'
        return super(PatientCard, self).create(vals)


    @api.depends('lab_test', 'mri_test')
    def _total_price_computation(self):
        for record in self:
            # add the mri_price and lab_test which are not aleady paid to be added and show the total
            total_price = sum(x.test_name.list_price for x in record.lab_test if not x.paid) + sum(x.test_type.list_price for x in record.mri_test if not x.paid)
            record.total_price = total_price

    def make_paid(self):
        for i in self.lab_test:
            i.paid= True 
        
        for i in self.mri_test:
            i.paid= True
        
    @api.depends('lab_test', 'mri_test')
    def _is_paid_computation(self):
        # check if all the lab_tess and mri_test are paid. 

        for record in self:
            record.is_paid = all(x.paid for x in record.lab_test) and all(x.paid for x in record.mri_test)