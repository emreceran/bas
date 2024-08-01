# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    tckimlikno = fields.Char(string="TC Kimlik No")

# class ResUsers(models.Model):
#     _inherit = 'res.users'
#
#     tckimlikno = fields.Char("TC Kimlik No", compute='_compute_tckimlikno', store=True)
#
#     @api.depends('partner_id', 'partner_id.tckimlikno')
#     def _compute_tckimlikno(self):
#         for applicant in self:
#             applicant.tckimlikno = applicant.partner_id.tckimlikno

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    tckimlikno = fields.Char("TC Kimlik No", compute='_compute_tckimlikno', store=True)
    partner_il = fields.Char("İl  ", compute='_compute_city', store=True)


    @api.depends('partner_id', 'partner_id.tckimlikno')
    def _compute_tckimlikno(self):
        for applicant in self:
            applicant.tckimlikno = applicant.partner_id.tckimlikno

    @api.depends('partner_id', 'partner_id.il_id')
    def _compute_city(self):
        for applicant in self:
            applicant.partner_il = applicant.partner_id.il_id.name

    partner_ilce = fields.Char("İlçe", compute='_compute_district', store=True)
    partner_lise = fields.Char("Lise", compute='_compute_highschool', store=True)
    partner_adres = fields.Char("Adres", compute='_compute_address', store=True)
    partner_birth_date = fields.Date("Doğum Günü", compute='_compute_birth_date', store=True)
    partner_birth_place = fields.Char("Doğum Yeri", compute='_compute_birth_place', store=True)
    partner_school_email = fields.Char("Okul Email", compute='_compute_school_email', store=True)
    partner_twitter_account = fields.Char("Twitter", compute='_compute_twitter_account', store=True)
    partner_facebook_account = fields.Char("Facebook", compute='_compute_facebook_account', store=True)
    partner_instagram_account = fields.Char("Instagram", compute='_compute_instagram_account', store=True)
    partner_linkedin_account = fields.Char("LinkedIn", compute='_compute_linkedin_account', store=True)
    partner_uni = fields.Char("Üniversite", compute='_compute_uni', store=True)
    partner_fak = fields.Char("Fakülte", compute='_compute_fak', store=True)
    partner_bolum = fields.Char("Bölüm", compute='_compute_bolum', store=True)
    partner_nationality = fields.Char("Uyruk", compute='_compute_nationality', store=True)
    partner_tc_kimlik_no = fields.Char("Tc Kimlik No", compute='_compute_tc_kimlik_no', store=True)
    partner_gender = fields.Selection([
        ('male', 'Erkek'),
        ('female', 'Kadın'),
    ], compute='_compute_gender', store=True)

    @api.depends('partner_id', 'partner_id.il_id')
    def _compute_city(self):
        for record in self:
            record.partner_il = record.partner_id.il_id.name

    @api.depends('partner_id', 'partner_id.ilce_id')
    def _compute_district(self):
        for record in self:
            record.partner_ilce = record.partner_id.ilce_id.name

    @api.depends('partner_id', 'partner_id.lise_id')
    def _compute_highschool(self):
        for record in self:
            record.partner_lise = record.partner_id.lise_id.name

    @api.depends('partner_id', 'partner_id.adres')
    def _compute_address(self):
        for record in self:
            record.partner_adres = record.partner_id.adres

    @api.depends('partner_id', 'partner_id.birth_date')
    def _compute_birth_date(self):
        for record in self:
            record.partner_birth_date = record.partner_id.birth_date

    @api.depends('partner_id', 'partner_id.birth_place')
    def _compute_birth_place(self):
        for record in self:
            record.partner_birth_place = record.partner_id.birth_place

    @api.depends('partner_id', 'partner_id.school_email')
    def _compute_school_email(self):
        for record in self:
            record.partner_school_email = record.partner_id.school_email

    @api.depends('partner_id', 'partner_id.twitter_account')
    def _compute_twitter_account(self):
        for record in self:
            record.partner_twitter_account = record.partner_id.twitter_account

    @api.depends('partner_id', 'partner_id.facebook_account')
    def _compute_facebook_account(self):
        for record in self:
            record.partner_facebook_account = record.partner_id.facebook_account

    @api.depends('partner_id', 'partner_id.instagram_account')
    def _compute_instagram_account(self):
        for record in self:
            record.partner_instagram_account = record.partner_id.instagram_account

    @api.depends('partner_id', 'partner_id.linkedin_account')
    def _compute_linkedin_account(self):
        for record in self:
            record.partner_linkedin_account = record.partner_id.linkedin_account

    @api.depends('partner_id', 'partner_id.uni_id')
    def _compute_uni(self):
        for record in self:
            record.partner_uni = record.partner_id.uni_id.name

    @api.depends('partner_id', 'partner_id.fak_id')
    def _compute_fak(self):
        for record in self:
            record.partner_fak = record.partner_id.fak_id.name

    @api.depends('partner_id', 'partner_id.bolum_id')
    def _compute_bolum(self):
        for record in self:
            record.partner_bolum = record.partner_id.bolum_id.name

    @api.depends('partner_id', 'partner_id.nationality_id')
    def _compute_nationality(self):
        for record in self:
            record.partner_nationality = record.partner_id.nationality_id.name

    @api.depends('partner_id', 'partner_id.tc_kimlik_no')
    def _compute_tc_kimlik_no(self):
        for record in self:
            record.partner_tc_kimlik_no = record.partner_id.tc_kimlik_no

    @api.depends('partner_id', 'partner_id.gender')
    def _compute_gender(self):
        for record in self:
            record.partner_gender = record.partner_id.gender


    def website_form_input_filter(self, request, values):
        current_user = request.env.user

        # Kullanıcının partner_id'sini alın
        values['partner_id'] = current_user.partner_id.id
        print("asasasa")

        if 'partner_name' in values:
            applicant_job = self.env['hr.job'].sudo().search(
                [('id', '=', values['job_id'])]).name if 'job_id' in values else False
            name = '%s - %s' % (values['partner_name'], applicant_job) if applicant_job else _("%s's Application",
                                                                                               values['partner_name'])
            values.setdefault('name', name)
        if values.get('job_id'):
            stage = self.env['hr.recruitment.stage'].sudo().search([
                ('fold', '=', False),
                '|', ('job_ids', '=', False), ('job_ids', '=', values['job_id']),
            ], order='sequence asc', limit=1)
            if stage:
                values['stage_id'] = stage.id
        return values
