cd questionnaire_api
python manage.py makemigrations &&
python manage.py migrate &&
gunicorn questionnaire_api.wsgi -b 0.0.0.0:8000