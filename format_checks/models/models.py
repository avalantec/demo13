# -*- coding: utf-8 -*-

from odoo import models, fields, api
import hashlib 
import time
import logging
import time
log = logging.getLogger(__name__)

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    
    company_name = fields.Char(string='Company name')
    company_address = fields.Char(string='Company Address')

    bank_name = fields.Char(string='Bank name')
    bank_address = fields.Char(string='Bank Address')
    hash_code = fields.Char(string='hash',readonly=True)

    def create_hash_code(self,values):
        data = ''
        if values.get('company_name') or  values.get('company_name') == False:
            data = data + values.get('company_name')
        else:
            data = data + str(self.company_name)

        if values.get('company_address') or values.get('company_address') == False:
            data = data + values.get('company_address')
        else:
            data = data + str(self.company_address)

        if values.get('bank_name') or values.get('bank_name') == False:
            data = data + values.get('bank_name')
        else:
            data = data + str(self.bank_name)

        if values.get('bank_address') or values.get('bank_address') == False:
            data = data + values.get('bank_address')
        else:
            data = data + str(self.bank_address)
        log.info("cadena {}".format(data))
        return hashlib.md5(data.encode()).hexdigest() 

    @api.model
    def create(self, vals):
        res = super(AccountJournal,self).create(vals)
        hash_code = self.create_hash_code(vals)
        self.update({'hash_code':hash_code})
        self.log_in_chatter(hash_code)
        return res

    def write(self, vals):
        log.info('vals {}'.format(vals))
        hash_code = self.create_hash_code(vals)
        if self.hash_code != hash_code:
            vals['hash_code'] = hash_code
            self.log_in_chatter(hash_code)
        res = super(AccountJournal, self).write(vals)
        return res
    
    def log_in_chatter(self,body):
        chatter = self.env['mail.message']
        chatter.create({
                        'res_id': self.id,
                        'model':'account.journal',
                        'body': body,
                       })


    

