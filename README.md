## 1 Repozitoriyani klonlash:
### git clone <repository-url>
### cd football_booking
## Virtual muhit yaratish va aktivatsiya qilish:
### python -m venv venv
### source venv/bin/activate  # Linux yoki MacOS uchun
### venv\Scripts\activate  # Windows uchun
## Zaruriy kutubxonalarni o‘rnatish:
### pip install -r requirements.txt
## Ma'lumotlar bazasini yaratish:
### DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'booking_db',
        'USER': 'booking_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
### python manage.py migrate
## Loyihani ishga tushirish:
### python manage.py runserver

