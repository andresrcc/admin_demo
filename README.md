# Django Admin Demo

Sample django app with a [template override](https://docs.djangoproject.com/en/5.2/howto/overriding-templates/).

## Quick Start

```bash

# install dependencies
python3 -m venv .venv  
source .venv/bin/activate
pip install -r requirements.txt

# Run setup
python3 setup.py

# Start server
python3 manage.py runserver --settings=mysite.settings
```

## Access

- **Hello World**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin`

