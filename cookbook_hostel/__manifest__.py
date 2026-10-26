{
    "name": "Hostel Management",
    "summary": "Manage hostels and their facilities",
    "description": """
        A training module for managing hostels.
    """,
    "author": "Mohamed Elhakim",
    "category": "Uncategorized",
    "version": "19.0.1.0.0",
    "depends": ["base"],
    "data": [
    "security/hostel_security.xml",
    "security/ir.model.access.csv",
"data/decimal_precision.xml",
    "views/hostel.xml",
],
    "demo": [],
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "auto_install": False,
}