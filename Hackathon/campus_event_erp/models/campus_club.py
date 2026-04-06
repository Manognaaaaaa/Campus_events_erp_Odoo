from odoo import api, fields, models


class CampusClubMember(models.Model):
    _name = 'campus.club.member'
    _description = 'Campus Club Member'
    _rec_name = 'partner_id'

    club_id = fields.Many2one('campus.club', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', required=True)
    role = fields.Selection(
        [
            ('president', 'President'),
            ('treasurer', 'Treasurer'),
            ('core', 'Core Team'),
            ('volunteer', 'Volunteer'),
        ],
        default='volunteer'
    )
    join_date = fields.Date(default=fields.Date.today)
    is_core = fields.Boolean(compute='_compute_is_core', store=True)

    @api.depends('role')
    def _compute_is_core(self):
        for record in self:
            record.is_core = record.role in ['president', 'treasurer', 'core']


class CampusClub(models.Model):
    _name = 'campus.club'
    _description = 'Campus Club'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    code = fields.Char(required=True, unique=True, tracking=True)
    faculty_advisor_id = fields.Many2one('res.partner', tracking=True)
    currency_id = fields.Many2one(
        'res.currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    total_budget = fields.Monetary(currency_field='currency_id', tracking=True)
    event_ids = fields.One2many('campus.event', 'club_id', readonly=True)
    member_ids = fields.One2many('campus.club.member', 'club_id', readonly=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Club code must be unique!')
    ]

    def action_open_events(self):
        """Open related events in a list view."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Events',
            'res_model': 'campus.event',
            'view_mode': 'tree,form',
            'domain': [('club_id', '=', self.id)],
            'context': {'default_club_id': self.id},
        }

    def action_open_members(self):
        """Open related members in a list view."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Members',
            'res_model': 'campus.club.member',
            'view_mode': 'tree,form',
            'domain': [('club_id', '=', self.id)],
            'context': {'default_club_id': self.id},
        }
