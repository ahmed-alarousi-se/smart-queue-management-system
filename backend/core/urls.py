from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # Root redirects
    path('', RedirectView.as_view(url='api/schema/swagger-ui/', permanent=False)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=False)),
    
    # My apps urls
    path('api/v1/', include('apps.api.urls')),
]
