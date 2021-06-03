from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from customer.api import viewsets
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


route = routers.DefaultRouter()
route.register(r'customers', viewsets.CustomerViewSet, basename='Customers')

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gabrielthe13@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),

    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documentation/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
