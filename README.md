## Editable Website Template

Editable Website POC / template with Django + htmx

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Home page has two editable ruch text fields, page model is updated on save and persisted in sqlite db.