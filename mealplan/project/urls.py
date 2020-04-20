from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

import private_storage.urls

urlpatterns = [
    path(settings.PRIVATE_STORAGE_URL, include(private_storage.urls)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls', namespace='core')),
    prefix_default_language=False,  # Don't display 'en/'
)
