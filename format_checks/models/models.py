# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    
    company_name = fields.Char(string='Company name')
    company_address = fields.Char(string='Company Address')

    bank_name = fields.Char(string='Bank name')
    bank_address = fields.Char(string='Bank Address')

    def create(self, values):
        res = super(AccountJournal, self).create(values)
        return res

    def write(self, values):
        res = super(AccountJournal, self).write()
        return res

    

