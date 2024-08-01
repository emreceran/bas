from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HrDepartment(models.Model):
    _inherit = 'hr.department'


    exceeds_capacity = fields.Boolean(string="Exceeds Capacity", compute='_compute_exceeds_capacity', store=True)
    capacity = fields.Integer(string='Kapasite', default=1)
    hami = fields.Char(string='Hami', default=1)
    total_employee = fields.Integer(compute='_compute_total_employee', string='Toplam Çalışan', store=True)
    hami_id = fields.Many2one('res.users', string="Hami")
    sorumlu_id = fields.Many2one('res.users', string="Sorumlu")

    full_icons = fields.Integer(compute='_compute_icons', string='Dolu İkonlar', store=True)
    extra_icons = fields.Integer(compute='_compute_icons', string='Ekstra İkonlar', store=True)
    icon_range = fields.Char(compute='_compute_icon_range', string='Icon Range')

    @api.depends('member_ids')
    def _compute_total_employee(self):
        for department in self:
            department.total_employee = len(department.member_ids)

    @api.depends('total_employee', 'capacity')
    def _compute_icons(self):
        for department in self:
            department.full_icons = min(department.total_employee, department.capacity)
            department.extra_icons = max(0, department.total_employee - department.capacity)

    @api.depends('capacity')
    def _compute_icon_range(self):
        for department in self:
            department.icon_range = ','.join(map(str, range(department.capacity)))

    @api.depends('total_employee', 'capacity')
    def _compute_exceeds_capacity(self):
        for department in self:
            department.exceeds_capacity = department.total_employee > department.capacity



    def _get_internal_users(self):
        users = self.env['res.users'].search([('groups_id', 'in', self.env.ref('base.group_user').id)])
        return [(user.id, user.name) for user in users]

    # @api.constrains('member_ids')
    # def _check_capacity(self):
    #     for department in self:
    #         if len(department.member_ids) > department.capacity:
    #             raise UserError(
    #                 _("Departmana kapasitesinden fazla kişi atadınız. Devam etmek istediğinizi onaylayınız veya lütfen işlemi iptal ediniz."))
    #
    # @api.model
    # def cancel_assignment(self, department_id):
    #     department = self.browse(department_id)
    #     if department:
    #         # Burada atamayı iptal etmek için gerekli işlemleri yapın
    #         pass





