# Odoo 19 Cookbook Practice

A learning project by Mohamed Elhakim, developed while studying Odoo 19 Development Cookbook (Sixth Edition). Work in progress through Chapter 4; not a production-ready application.

## Hostel Management

The `cookbook_hostel` addon implements:
- Hostel records, address and state, floor count, type, notes and archiving.
- List, form and search views with navigation menus.
- Display names combining hostel name and code.
- Opening dates and inspection appointments.
- Configurable rating precision using Decimal Accuracy.
- Manager CRUD access and a read-only Hostel User group.

The only declared dependency is `base`. No Odoo core, Enterprise source, database backups or book files are included.

## Installation

1. Use an existing Odoo 19 installation and a development database.
2. Clone this repository and add its absolute directory to `addons_path` in your local configuration.
3. Restart Odoo, enable developer mode and update the Apps List.
4. Search for `cookbook_hostel` (remove the Apps filter if needed) and install Hostel Management.
5. Open Hostel Training > Hostels.

For later updates, restart Odoo after Python changes and upgrade the installed addon.

Linux example (replace paths and database name with your own):

```bash
python odoo-bin -c /path/to/odoo.conf -d training_db -u cookbook_hostel --stop-after-init
```

## Validation and limitations

Python syntax, XML parsing and manifest data-file existence checked during repository preparation. The learner has exercised record creation, display-name recomputation and date defaults in a local Odoo 19 instance. No automated Odoo integration suite has been run.

Ordinary-user access checks remain pending. Hostel codes are not yet unique; rating ranges and nonnegative floor counts are not constrained. These are later learning exercises. The training administrator is assigned the Hostel Manager group by the module data.

## Learning roadmap

- [x] Module structure, manifest, model and views
- [x] Access groups and model access declarations
- [x] Display names and basic fields
- [x] Configurable float precision
- [ ] Monetary and relational fields
- [ ] Constraints and computed fields
- [ ] Inheritance
- [ ] Independent API integration and OWL portfolio projects after the book

The addon manifest declares LGPL-3. This repository contains the training addon, not the book itself.
