from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
    title='Movie API',
    default_version='v1',
    description='API para recordar Django and land my first job!',
    terms_of_service='https://policies.google.com/terms/',
    contact=openapi.Contact(email='maesgaab@gmail.com'),
    license=openapi.License('MIT')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    # path('swagger.json/',schema_view.with_ui(cache_timeout=0), name='swagger-json'),
]