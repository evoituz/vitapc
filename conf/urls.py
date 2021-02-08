from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from apps.restapi.urls import urlpatterns as swagger_urls


# mobile_app_view = get_swagger_view(title='Kimit mobile API', url='/api/v1/', patterns=mobile_urls)

swagger = get_swagger_view(title='Web API', url='/api/v1/web/', patterns=swagger_urls)

urlpatterns = [
    path('swagger/', swagger),
    path('admin/', admin.site.urls),
    path('api/v1/web/', include('apps.restapi.urls', namespace='swagger'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
