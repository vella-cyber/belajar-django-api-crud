from django.contrib import admin
from django.urls import path
from api import views  # Ganti 'api' dengan nama folder aplikasi tempat views.py kamu berada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/asisten/', views.asisten_api, name='asisten_api'),
]