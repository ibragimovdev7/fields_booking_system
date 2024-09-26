# Python 3.9 slim image'dan foydalanamiz
FROM python:3.9-slim

# Ishchi katalogni yaratamiz
WORKDIR /app

# Tizim kutubxonalarini o'rnatamiz (psycopg2 kabi paketlar uchun kerak bo'ladi)
RUN apt-get update && apt-get install -y gcc libpq-dev

# Pipni yangilab olamiz
RUN pip install --upgrade pip

# `requirements.txt` faylini ko'chiramiz va kutubxonalarni o'rnatamiz
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Ilovaning barcha fayllarini ishchi katalogga ko'chiramiz
COPY . /app/

# Django static fayllarini yig'ish uchun buyruq
RUN python manage.py collectstatic --noinput

# Portni ochamiz (Agar kerak bo'lsa)
EXPOSE 8000

# Django ilovasini ishga tushirish komandasi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
