# -*- coding: utf-8 -*-

from odoo import models, fields, api
import hashlib 
import time

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    
    company_name = fields.Char(string='Company name')
    company_address = fields.Char(string='Company Address')

    bank_name = fields.Char(string='Bank name')
    bank_address = fields.Char(string='Bank Address')
    hash_code = fields.Char(string='hash',readonly=True)

    def create_hash_code(self,values):
        data = str(values['company_name'] or '') + str(values['self.company_address'] or '') + str(values['bank_name'] or '') + str(values['bank_address'] or '')
        return hashlib.md5(data.encode()).hexdigest() 

    def create(self, values):
        hash_code = self.create_hash_code(values)
        if self.hash_code != hash_code:
            values['hash_code'] = hash_code
            self.log_in_chatter(hash_code)
        res = super(AccountJournal, self).create(values)
        return res

    def write(self, values):
        hash_code = self.create_hash_code(values)
        if self.hash_code != hash_code:
            values['hash_code'] = hash_code
            self.log_in_chatter(hash_code)
        res = super(AccountJournal, self).write(values)
        return res
    
    def log_in_chatter(self,body):
        chatter = self.env['mail.message']
        chatter.create({
                        'res_id': self.id,
                        'model':'account.journal',
                        'body': body,
                       })


    

