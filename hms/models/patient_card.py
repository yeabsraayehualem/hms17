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

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.card') or 'New'
        return super(PatientCard, self).create(vals)
