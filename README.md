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

Run the following test to check all the end-points return the correct http status code 

```bash
python manage.py test
```

## How to deploy
1. Prepare for production

   Set DEBUG = False in settings.py.
   Set ALLOWED_HOSTS to your domain or server IP.
   
2. Choose a Hosting Platform
3. Install a Production WSGI Server
4. Set Up a Web Server6. Apply Migrations
5. Start the Application
6. Configure Environment Variables
7. Secure Your Deployment
