# littlelemon

Final project - Django REST API for the Little Lemon restaurant.

## Setup

```bash
pip install -r requirements.txt
cd littlelemon
python manage.py migrate
python manage.py runserver
```

## Test the following endpoints

- `restaurant/menu/` - requires token auth
- `restaurant/booking/` - requires token auth
- `restaurant/users/` - requires token auth
- `auth/users/` - register a user
- `auth/token/login/` - obtain an auth token (POST `username`/`password`)
- `restaurant/` - public landing page

The project uses SQLite (no external database server required). Run the
test suite with `python manage.py test`.
