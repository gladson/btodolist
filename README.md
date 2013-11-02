btodolist
=========

Simple web based todo list app.
-------------------------

Backend:

* django 1.5.5
* django-rest-framework 2.3.8
* sqlite3


Frontend:
* AngularJS 1.0.8
* AngularUI ui-bootstrap 0.6.0
* Twitter Bootstrap 2.3.2

Setup:
-------------------------
### Virtualenv and deps:
```bash
python -m virtualenv --no-site-packages PATH_TO_VENV
. PATH_TO_VENV/bin/activate
pip install -r PATH_TO_TODOLIST/requirements.txt
```

### Start app(local):
```bash
python PATH_TO_TODOLIST/btodolist/manage.py syncdb
python PATH_TO_TODOLIST/btodolist/manage.py runserver
```

### Start app(web):
* Change database path.
* Disable debug mode.
* Disable rest_framework browsable interface.
* Configure Apache with mod_wsgi (or use gunicorn).
