from odoo import fields, models


class CampusSponsor(models.Model):
    _name = 'campus.sponsor'
    _description = 'Campus Event Sponsor'
    _rec_name = 'name'

    name = fields.Char(required=True)
    event_id = fields.Many2one('campus.event', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', required=True)
    amount = fields.Monetary(required=True, currency_field='currency_id')
    benefits = fields.Text()
    currency_id = fields.Many2one(
        'res.currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
