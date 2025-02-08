from odoo import models,fields,api      

class Employee(models.Model):
    _inherit= 'hr.employee'

    emp_type = fields.Selection([
        (i,i.capitalize()) for i in ['nurse','doctor','secretary','cashier']
    ])