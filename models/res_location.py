# from odoo import models, fields, api
#
# class ResIlce(models.Model):
#     _name = 'res.ilce'
#     _description = 'İlçe'
#
#     name = fields.Char(string="İlçe Adı", required=True)
#     mahalle_ids = fields.One2many('res.mahalle', 'ilce_id', string="Mahalleler")
#
# class ResMahalle(models.Model):
#     _name = 'res.mahalle'
#     _description = 'Mahalle'
#
#     name = fields.Char(string="Mahalle Adı", required=True)
#     ilce_id = fields.Many2one('res.ilce', string="İlçe", required=True)
#
# class HrDepartment(models.Model):
#     _inherit = 'hr.department'
#
#     ilce_id = fields.Many2one('res.ilce', string="İlçe")
#     mahalle_id = fields.Many2one('res.mahalle', string="Mahalle")
#     address_line = fields.Char(string="Adres Satırı")
#
#     @api.onchange('ilce_id')
#     def _onchange_ilce_id(self):
#         self.mahalle_id = False
#         return {'domain': {'mahalle_id': [('ilce_id', '=', self.ilce_id.id)]}}


from odoo import models, fields, api

class ResIlce(models.Model):
    _name = 'res.ilce'
    _description = 'İlçe'

    name = fields.Char(string="İlçe Adı", required=True)
    mahalle_ids = fields.One2many('res.mahalle', 'ilce_id', string="Mahalleler")

class ResMahalle(models.Model):
    _name = 'res.mahalle'
    _description = 'Mahalle'

    name = fields.Char(string="Mahalle Adı", required=True)
    ilce_id = fields.Many2one('res.ilce', string="İlçe", required=True)

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    ilce_id = fields.Many2one('res.ilce', string="İlçe")
    mahalle_id = fields.Many2one('res.mahalle', string="Mahalle")
    address_line = fields.Char(string="Adres Satırı")
    display_location = fields.Char(string="Konum", compute="_compute_display_location")

    @api.onchange('ilce_id')
    def _onchange_ilce_id(self):
        self.mahalle_id = False
        return {'domain': {'mahalle_id': [('ilce_id', '=', self.ilce_id.id)]}}

    @api.depends('ilce_id', 'mahalle_id')
    def _compute_display_location(self):
        for record in self:
            if record.ilce_id and record.mahalle_id:
                record.display_location = f"{record.ilce_id.name} / {record.mahalle_id.name} Mahallesi"
            elif record.ilce_id:
                record.display_location = record.ilce_id.name
            else:
                record.display_location = ''
