# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Il(models.Model):
    _name = 'bas.il'
    _description = 'Il'

    name = fields.Char(string='Name', required=True)
    ilce_ids = fields.One2many('bas.ilce', 'il_id', string='İlçeler')
    lise_ids = fields.One2many('bas.lise', 'il_id', string='Liseler')
    manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    user_ids = fields.One2many('res.users', 'il_id', string='Öğrenciler')
    user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')

    @api.depends('user_ids')
    def _compute_user_count(self):
        for il in self:
            il.user_count = len(il.user_ids)

    def action_view_users(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'İldeki Öğrenciler',
            'res_model': 'res.users',
            'view_mode': 'tree',
            'domain': [('il_id', '=', self.id)],
            'context': dict(self.env.context, create=False)
        }

class Ilce(models.Model):
    _name = 'bas.ilce'
    _description = 'Ilce'

    name = fields.Char(string='Name', required=True)
    il_id = fields.Many2one('bas.il', string='İl', required=True)
    lise_ids = fields.One2many('bas.lise', 'ilce_id', string='Liseler')
    manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    user_ids = fields.One2many('res.users', 'ilce_id', string='Öğrenciler')
    user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')

    @api.depends('user_ids')
    def _compute_user_count(self):
        for ilce in self:
            ilce.user_count = len(ilce.user_ids)

    def action_view_users(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'İlçedeki Öğrenciler',
            'res_model': 'res.users',
            'view_mode': 'tree,form',
            'view_id': self.env.ref('bas.view_ilce_users_tree').id,
            'domain': [('ilce_id', '=', self.id)],
            'context': dict(self.env.context, create=False)
        }

class Lise(models.Model):
    _name = 'bas.lise'
    _description = 'Lise'

    name = fields.Char(string='Name', required=True)
    il_id = fields.Many2one('bas.il', string='İl', required=True)
    ilce_id = fields.Many2one('bas.ilce', string='İlçe')
    manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    user_ids = fields.One2many('res.users', 'lise_id', string='Öğrenciler')
    user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')
    adres = fields.Char(string='adres',)

    @api.depends('user_ids')
    def _compute_user_count(self):
        for lise in self:
            lise.user_count = len(lise.user_ids)

    def action_view_users(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lisedeki Öğrenciler',
            'res_model': 'res.users',
            'view_mode': 'tree,form',
            'domain': [('lise_id', '=', self.id)],
            'context': dict(self.env.context, create=False)
        }


# ------------------------------------------------------------------------------------------------------------------


class Uni(models.Model):
    _name = 'bas.uni'
    _description = 'Üniversite'

    name = fields.Char(string='Name', required=True)
    fak_ids = fields.One2many('bas.fak', 'uni_id', string='Fakülteler')
    bolum_ids = fields.One2many('bas.bolum', 'uni_id', string='Bölümler')
    # manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    # user_ids = fields.One2many('res.users', 'uni_id', string='Öğrenciler')
    # user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')

    # @api.depends('user_ids')
    # def _compute_user_count(self):
    #     for uni in self:
    #         uni.user_count = len(uni.user_ids)
    #
    # def action_view_users(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Üniversitedeki Öğrenciler',
    #         'res_model': 'res.users',
    #         'view_mode': 'tree',
    #         'domain': [('uni_id', '=', self.id)],
    #         'context': dict(self.env.context, create=False)
    #     }

class Fak(models.Model):
    _name = 'bas.fak'
    _description = 'Fakülte'

    name = fields.Char(string='Name', required=True)
    uni_id = fields.Many2one('bas.uni', string='Üniversite', required=True)
    bolum_ids = fields.One2many('bas.bolum', 'fak_id', string='Bölümler')
    # manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    # user_ids = fields.One2many('res.users', 'fak_id', string='Öğrenciler')
    # user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')
    #
    # @api.depends('user_ids')
    # def _compute_user_count(self):
    #     for fak in self:
    #         fak.user_count = len(fak.user_ids)
    #
    # def action_view_users(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Fakültedeki Öğrenciler',
    #         'res_model': 'res.users',
    #         'view_mode': 'tree,form',
    #         'view_id': self.env.ref('bas.view_fak_users_tree').id,
    #         'domain': [('fak_id', '=', self.id)],
    #         'context': dict(self.env.context, create=False)
    #     }

class Bolum(models.Model):
    _name = 'bas.bolum'
    _description = 'Bölüm'

    name = fields.Char(string='Name', required=True)
    uni_id = fields.Many2one('bas.uni', string='Üniversite', required=True)
    fak_id = fields.Many2one('bas.fak', string='Fakülte')
    # manager_id = fields.Many2one('res.users', string='Yönetici', domain="[('groups_id', 'in', [1])]")  # 1 is the ID of the internal user group
    # user_ids = fields.One2many('res.users', 'bolum_id', string='Öğrenciler')
    # user_count = fields.Integer(string='Öğrenci Sayısı', compute='_compute_user_count')
    #
    # @api.depends('user_ids')
    # def _compute_user_count(self):
    #     for bolum in self:
    #         bolum.user_count = len(bolum.user_ids)
    #
    # def action_view_users(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Bölümdeki Öğrenciler',
    #         'res_model': 'res.users',
    #         'view_mode': 'tree,form',
    #         'domain': [('bolum_id', '=', self.id)],
    #         'context': dict(self.env.context, create=False)
    #     }





