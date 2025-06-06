# payment_api

## How to run
```bash
python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework
django-admin startproject payment_api
```
cd payment_api
```bash
python manage.py startapp payments
python manage.py migrate
python manage.py runserver
```
