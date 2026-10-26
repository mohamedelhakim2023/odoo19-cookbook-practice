from odoo import models, fields, api

class Hostel(models.Model):
    _name = "cookbook.hostel"
    _description = "Information about hostel"

    _rec_name = "hostel_code"
    _order = "name, id"
    _rec_names_search = ["name", "hostel_code"]

    name = fields.Char(string="Hostel Name", required=True)
    hostel_code = fields.Char(
        string="Code",
        required=True,
    )
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street 2")
    state_id = fields.Many2one(
        "res.country.state",
        string="State",
    )
    hostel_floors = fields.Integer(
        string="Total Floors",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    type = fields.Selection(
        selection=[
            ("male", "Boys"),
            ("female", "Girls"),
            ("common", "Common"),
        ],
        string="Type",
        required=True,
        default="common",
    )

    other_info = fields.Text(
        string="Other Information",
        help="Enter additional information about the hostel",
        copy=False,
    )
    opened_on = fields.Date(
        string="Opening Date",
        default=fields.Date.context_today,
    )

    inspection_at = fields.Datetime(
        string="Inspection Appointment",
    )
    hostel_rating = fields.Float(
        string="Hostel Average Rating",
        digits="Hostel Rating",
    )


    @api.depends("name", "hostel_code")
    def _compute_display_name(self):
        for record in self:
            name = record.name or ""

            if record.hostel_code:
                name = f"{name} ({record.hostel_code})"

            record.display_name = name