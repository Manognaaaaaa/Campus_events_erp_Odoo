from odoo import api, fields, models


class CampusEventBudgetLine(models.Model):
    _name = 'campus.event.budget.line'
    _description = 'Campus Event Budget Line'

    name = fields.Char(required=True)
    event_id = fields.Many2one('campus.event', required=True, ondelete='cascade')
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
    amount = fields.Monetary(required=True, currency_field='currency_id')
    currency_id = fields.Many2one(
        'res.currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )


class CampusEvent(models.Model):
    _name = 'campus.event'
    _description = 'Campus Event'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    STATE_SELECTION = [
        ('idea', 'Idea'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    name = fields.Char(required=True, tracking=True, search=True)
    club_id = fields.Many2one('campus.club', required=True, ondelete='cascade', tracking=True, search=True)
    date = fields.Date(required=True, tracking=True, search=True)
    end_date = fields.Date(tracking=True, search=True)
    venue = fields.Char(tracking=True, search=True)
    state = fields.Selection(STATE_SELECTION, default='idea', tracking=True)
    planned_attendees = fields.Integer()
    actual_attendees = fields.Integer()
    # File/Image upload support
    event_logo = fields.Image(attachment=True)
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'event_attachment_rel',
        'event_id',
        'attachment_id',
        string='Additional Files'
    )
    budget_line_ids = fields.One2many('campus.event.budget.line', 'event_id', readonly=False)
    purchase_request_ids = fields.One2many('campus.purchase.request', 'event_id', readonly=False)
    sponsor_ids = fields.One2many('campus.sponsor', 'event_id', readonly=False)
    currency_id = fields.Many2one(
        'res.currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    planned_budget_total = fields.Monetary(
        compute='_compute_planned_budget_total',
        currency_field='currency_id',
        store=True
    )
    actual_spent_total = fields.Monetary(
        compute='_compute_actual_spent_total',
        currency_field='currency_id',
        store=True
    )
    sponsorship_total = fields.Monetary(
        compute='_compute_sponsorship_total',
        currency_field='currency_id',
        store=True
    )
    net_cost = fields.Monetary(
        compute='_compute_net_cost',
        currency_field='currency_id',
        store=True
    )

    @api.depends('budget_line_ids.amount')
    def _compute_planned_budget_total(self):
        for record in self:
            record.planned_budget_total = sum(
                line.amount for line in record.budget_line_ids
            )

    @api.depends('purchase_request_ids.amount', 'purchase_request_ids.state')
    def _compute_actual_spent_total(self):
        for record in self:
            record.actual_spent_total = sum(
                req.amount for req in record.purchase_request_ids
                if req.state in ['approved', 'paid']
            )

    @api.depends('sponsor_ids.amount')
    def _compute_sponsorship_total(self):
        for record in self:
            record.sponsorship_total = sum(sponsor.amount for sponsor in record.sponsor_ids)

    @api.depends('actual_spent_total', 'sponsorship_total')
    def _compute_net_cost(self):
        for record in self:
            record.net_cost = record.actual_spent_total - record.sponsorship_total

    @api.constrains('date', 'end_date', 'venue')
    def _check_venue_availability(self):
        """Prevent double-booking of the same venue.
        
        Checks if another event with the same venue has overlapping date ranges.
        Raises ValidationError if overlap is detected.
        """
        for record in self:
            # Skip check if venue is not set
            if not record.venue:
                continue
            
            # Determine the date range for this event
            event_start = record.date
            event_end = record.end_date or record.date
            
            # Find other approved or confirmed events for the same venue
            overlapping_events = self.search([
                ('id', '!=', record.id),
                ('venue', '=', record.venue),
                ('state', 'not in', ['cancelled']),  # Ignore cancelled events
                '|',
                ('date', '<=', event_end),  # Other event starts before or on our end
                ('end_date', '=', False),
            ])
            
            # Filter for actual overlaps
            for other_event in overlapping_events:
                other_start = other_event.date
                other_end = other_event.end_date or other_event.date
                
                # Check if date ranges overlap
                if not (event_end < other_start or event_start > other_end):
                    from odoo.exceptions import ValidationError
                    raise ValidationError(
                        f"Venue '{record.venue}' is already booked from "
                        f"{other_event.date} to {other_event.end_date or other_event.date} "
                        f"for event '{other_event.name}'. "
                        f"Please choose a different venue or date."
                    )

    def action_to_approve(self):
        """Move event to 'To Approve' state."""
        self.write({'state': 'to_approve'})

    def action_approve(self):
        """Move event to 'Approved' state."""
        self.write({'state': 'approved'})

    def action_complete(self):
        """Move event to 'Completed' state."""
        self.write({'state': 'completed'})

    def action_cancel(self):
        """Move event to 'Cancelled' state."""
        self.write({'state': 'cancelled'})

