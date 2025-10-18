from django.conf import settings


def app_settings(request):
    return {
        "app_name": settings.APP_NAME,
    }
