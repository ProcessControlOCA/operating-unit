# © 2019 ForgeFlow S.L.
# - Jordi Ballester Alomar
# © 2019 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "Operating Unit in Sales",
    "version": "16.0.1.0.1",
    "summary": "An operating unit (OU) is an organizational entity part of a "
    "company",
    "author": "ForgeFlow, "
    "Serpent Consulting Services Pvt. Ltd.,"
    "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/operating-unit",
    "category": "Sales Management",
    "depends": ["sale", "account_operating_unit", "sales_team_operating_unit"],
    "data": [
        "security/sale_security.xml",
        "views/sale_view.xml",
        "views/sale_report_view.xml",
    ],
    "installable": True,
}
