"""
URL configuration for car_inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
    title='Car Inventory System',
    default_version= 1,
    terms_of_service='https://www.google.com/policies/terms/',
    contact=openapi.Contact(email='favouroghenevwoke@gmail.com'),
    license=openapi.License(name='Car Inventory System'),
    ),
    public= True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes= []

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.router')),
    path('car/', include('car.router')),
    path('swagger/noui', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)