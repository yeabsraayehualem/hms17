from odoo import models, fields, api
from datetime import date

class Patients(models.Model):
    _name = "hospital.patient"
    _description = "Patient Information"
    _order="name desc"

    patient_name = fields.Char(string="Name", required=True)
    name = fields.Char(string="Reference", readonly=True, copy=False, default="New")
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    phone_number = fields.Char(string="Phone Number")
    marital_status = fields.Selection([(i,i.capitalize()) for i in ['maried','unmaried']], string="Marital Status")
    medical_history = fields.One2many('patient.medical.history', 'patient_id', string="Medical History")
    doctor_id = fields.Many2one('hr.employee', string="Doctor", domain=[('emp_type','=','doctor')])
    address = fields.Text(string="Address")
    emergency_contact = fields.Char(string="Emergency Contact")
    emergency_contact_number = fields.Char(string="Emergency Contact Number")
    insurance_provider = fields.Char(string="Insurance Provider")
    insurance_number = fields.Char(string="Insurance Number")
    emergency_contact_relationship = fields.Selection([(i,i.capitalize()) for i in ['husband','wife','father','mother','brother','sister','child','grandfather','grandmother']], string="Emergency Contact Relationship")
    count_cards= fields.Integer(compute="_count_cards")
    state = fields.Selection([
        ('new', 'New'),
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged'),
    ], string="Status", default='new')

    def _count_cards(self):
        for rec in self:
            rec.count_cards = self.env['patient.card'].search_count([('patient_id', '=', rec.id)])
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = date.today().year - rec.date_of_birth.year
            else:
                rec.age = 0

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'
        return super(Patients, self).create(vals)


    def create_card(self):
        self.env['patient.card'].create({
            'patient_id': self.id,  
        })

    def to_card(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Patient Cards',
            'res_model': 'patient.card',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'target': 'current',
        }
class PatientMedicalHistory(models.Model):
    _name = "patient.medical.history"
    _description = "Patient Medical History"

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    diagnosis = fields.Char(string="Diagnosis")
    treatment = fields.Text(string="Treatment")
    date = fields.Date(string="Date")
