FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ="UTC"

WORKDIR /app
COPY . /app

HEALTHCHECK --interval=30s --timeout=30s --start-period=10s --retries=3 \
             CMD curl -f http://127.0.0.1:8000/healthcheck || exit 1


RUN pip install -r requirements.txt \
    && python manage.py collectstatic --noinput
#    && python manage.py createcachetable \
#    && python manage.py makemigrations --merge \
#    && python manage.py migrate
