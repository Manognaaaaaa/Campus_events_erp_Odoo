from odoo import api, fields, models


class CampusPurchaseRequest(models.Model):
    _name = 'campus.purchase.request'
    _description = 'Campus Purchase Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    STATE_SELECTION = [
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('paid', 'Paid'),
    ]

    name = fields.Char(
        required=True,
        readonly=True,
        default='New',
        tracking=True
    )
    event_id = fields.Many2one('campus.event', required=True, ondelete='cascade', tracking=True)
    vendor_id = fields.Many2one('res.partner', tracking=True)
    description = fields.Text()
    category = fields.Selection(
        [
            ('decor', 'Décor'),
            ('catering', 'Catering'),
            ('printing', 'Printing'),
            ('tech', 'Technology'),
            ('prizes', 'Prizes'),
            ('other', 'Other'),
        ],
        default='other'
    )
    amount = fields.Monetary(required=True, currency_field='currency_id', tracking=True)
    currency_id = fields.Many2one(
        'res.currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    state = fields.Selection(STATE_SELECTION, default='draft', tracking=True)
    requester_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('campus.purchase.request.seq')
        return super().create(vals_list)

    def action_submit(self):
        """Submit the purchase request for approval."""
        self.write({'state': 'to_approve'})

    def action_approve(self):
        """Approve the purchase request."""
        self.write({'state': 'approved'})

    def action_reject(self):
        """Reject the purchase request."""
        self.write({'state': 'rejected'})

    def action_paid(self):
        """Mark the purchase request as paid."""
        self.write({'state': 'paid'})

