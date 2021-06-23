import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-operating-unit",
    description="Meta package for oca-operating-unit Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-account_financial_report_operating_unit',
        'odoo14-addon-account_operating_unit',
        'odoo14-addon-analytic_operating_unit',
        'odoo14-addon-contract_operating_unit',
        'odoo14-addon-hr_expense_operating_unit',
        'odoo14-addon-operating_unit',
        'odoo14-addon-operating_unit_access_all',
        'odoo14-addon-purchase_operating_unit',
        'odoo14-addon-purchase_request_operating_unit',
        'odoo14-addon-sales_team_operating_unit',
        'odoo14-addon-stock_operating_unit',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
