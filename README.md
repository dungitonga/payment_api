## payment_api

How to run

python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework
django-admin startproject payment_api
cd payment_api
python manage.py startapp payments
# Add code above to respective files
python manage.py migrate
python manage.py runserver
