from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.site_header = "Адмнистрирование tbo_dash"
admin.site.site_title = "Адмнистрирование tbo_dash"
admin.site.index_title = "tbo_dash"

ver_tag = 'v1'
prefix = f'api/{ver_tag}/'

schema_view = get_schema_view(
    openapi.Info(
        title="Весовая API",
        default_version=ver_tag,
        contact=openapi.Contact(
            name="Nikolay Bely",
            url="https://github.com/alldevic",
            email="beliy_ns@kuzro.ru"),
        license=openapi.License(
            name="MIT License",
            url="https://github.com/alldevic/tbo_dash/tbo_dash/master/LICENSE"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(prefix, schema_view.with_ui('swagger',
                                     cache_timeout=0), name='docs-ui'),
    re_path(rf'^{prefix}tbo_dash_openapi(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(f'{prefix}auth/', include('djoser.urls.authtoken')),
    path(f'{prefix}', include('djoser.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # Silk profiler
    urlpatterns = [
        path('silk/', include('silk.urls', namespace='silk')),
    ] + urlpatterns
