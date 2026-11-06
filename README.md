# The Ivory Table

The Ivory Table is a Django website for a Nairobi restaurant concept. The current codebase establishes the shared visual foundation and page routing so the team can build the restaurant pages on top of it.

## Current status

The project is in the frontend scaffolding stage.

- The Django project is `Ivory`, with three apps: `core`, `menu`, and `reservations`.
- The shared project-level layout is `templates/base.html`. It contains the site navigation and footer, loads Bootstrap and `static/css/main.css`, and provides template blocks.
- The homepage is in `core/templates/home.html` and extends `base.html`.
- The homepage and shared navigation use Django named URL routes.
- Page views and URL patterns exist for home, about, order, menu, and reservations.
- `static/css/main.css` contains the current charcoal, ivory, and gold visual system and homepage styles.
- The `about.html`, `order.html`, `menu.html`, and `reservations.html` files are placeholders and still need page content and presentation.
- The app model files do not yet define restaurant data. There is no application JavaScript yet.

The current routes are:

| Page | URL | Django URL name | Owning app |
| --- | --- | --- | --- |
| Home | `/` | `core:home` | `core` |
| About | `/about/` | `core:about` | `core` |
| Order | `/order/` | `core:order` | `core` |
| Menu | `/menu/` | `menu:menu` | `menu` |
| Reservations | `/reservations/` | `reservations:reservations` | `reservations` |
| Django admin | `/admin/` | — | Django |

## Project layout

```text
The-Ivory-Table/
├── Ivory/                    # Django settings and root URL configuration
├── core/                     # Home, about, and order pages
│   └── templates/             # home.html, about.html, order.html
├── menu/                     # Menu page
│   └── templates/             # menu.html
├── reservations/             # Reservations page
│   └── templates/             # reservations.html
├── templates/
│   └── base.html              # Shared site layout
├── static/
│   └── css/main.css           # Shared styles
├── manage.py
├── requirements.txt
└── db.sqlite3                 # Local SQLite database (ignored by Git)
```

## Run locally

From the project root, create and activate a virtual environment, then install the pinned dependencies.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py check
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. If `.venv` already exists, activate it and continue from dependency installation. The `.venv` directory and local SQLite database are excluded from version control.

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py check
python manage.py runserver
```

## Template contribution guide

Keep the shared navigation and footer in `templates/base.html`. App pages should extend that layout rather than duplicate it. For example:

```django
{% extends "base.html" %}

{% block title %}Menu | The Ivory Table{% endblock %}

{% block meta_description %}Explore the menu at The Ivory Table.{% endblock %}

{% block content %}
  <!-- Page-specific content -->
{% endblock %}
```

Use `{% url %}` with the route names above for internal links. Use `{% load static %}` and `{% static '...' %}` for local images, styles, and scripts. The shared layout currently supports `title`, `meta_description`, `extra_css`, `content`, and `extra_js` blocks.

## Next contributional steps

1. Have the page owners build the menu, about, order, and reservations templates using the shared layout and agree on navigation, page content, and any form fields.
2. Integrate the templates and check that each named route renders.
3. Define the data requirements, then add Django models for menu items, reservations, and orders. Create and apply migrations after the model design is agreed.
4. Add Django views and forms to validate and save reservations and orders. Use JavaScript for optional interface enhancements such as menu filtering, cart behavior, and client-side feedback; Django remains responsible for validation and persistence.
5. Revisit the copy, imagery, and business details with the team before treating placeholder content as final.

## Dependencies

Dependencies are pinned in `requirements.txt` (Django and its required packages). The shared layout currently loads Bootstrap and Google Fonts from external CDNs. The project uses SQLite in local development. There are no restaurant-specific database models or JavaScript behaviors yet.
