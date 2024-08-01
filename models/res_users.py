from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    il_id = fields.Many2one(related='partner_id.il_id', inherited=True, readonly=False)
    ilce_id = fields.Many2one(related='partner_id.ilce_id', inherited=True, readonly=False)
    lise_id = fields.Many2one(related='partner_id.lise_id', inherited=True, readonly=False)
    # ilce_id = fields.Many2one('bas.ilce', string='District')
    # lise_id = fields.Many2one('bas.lise', string='School')

    adres = fields.Char(related='partner_id.adres', inherited=True, readonly=False)
    birth_date = fields.Date(related='partner_id.birth_date', inherited=True, readonly=False)
    birth_place = fields.Char(related='partner_id.birth_place', inherited=True, readonly=False)
    school_email = fields.Char(related='partner_id.school_email', inherited=True, readonly=False)
    twitter_account = fields.Char(related='partner_id.twitter_account', inherited=True, readonly=False)

    facebook_account = fields.Char(related='partner_id.facebook_account', inherited=True, readonly=False)
    instagram_account = fields.Char(related='partner_id.instagram_account', inherited=True, readonly=False)
    linkedin_account = fields.Char(related='partner_id.linkedin_account', inherited=True, readonly=False)

    uni_id = fields.Many2one(related='partner_id.uni_id', inherited=True, readonly=False)
    fak_id = fields.Many2one(related='partner_id.fak_id', inherited=True, readonly=False)
    bolum_id = fields.Many2one(related='partner_id.bolum_id', inherited=True, readonly=False)

    managed_il_ids = fields.One2many(related='partner_id.managed_il_ids', inherited=True, readonly=False)
    managed_ilce_ids = fields.One2many(related='partner_id.managed_ilce_ids', inherited=True, readonly=False)
    managed_lise_ids = fields.One2many(related='partner_id.managed_lise_ids', inherited=True, readonly=False)

    nationality_id = fields.Many2one(related='partner_id.nationality_id', inherited=True, readonly=False)
    tc_kimlik_no = fields.Char(related='partner_id.tc_kimlik_no', inherited=True, readonly=False)
    gender = fields.Selection(related='partner_id.gender', inherited=True, readonly=False)

    # @api.constrains('tc_kimlik_no')
    # def _check_tc_kimlik_no(self):
    #     for record in self:
    #         if record.tc_kimlik_no:
    #             if not record.tc_kimlik_no.isdigit():
    #                 raise ValidationError('TC Kimlik No sadece rakamlardan oluşmalıdır.')
    #             if len(record.tc_kimlik_no) != 11:
    #                 raise ValidationError('TC Kimlik No 11 haneli olmalıdır.')
    #
    # def action_grant_karma(self):
    #     self.ensure_one()
    #     self.karma += 10  # Örneğin, 10 karma puanı ekleyin


