from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home, contacts
from django.conf import settings
from django.conf.urls.static import static

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
