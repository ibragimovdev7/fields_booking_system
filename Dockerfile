# Base image sifatida Python 3.9 versiyasidan foydalanamiz
FROM python:3.9-slim

# Ishchi katalogni yaratamiz
WORKDIR /app

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
