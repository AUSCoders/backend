from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("models/", include('djangomodels.urls')),
    path("validators/", include('validators.urls')),
    
]
