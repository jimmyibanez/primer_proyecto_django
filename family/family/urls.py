
from django.contrib import admin
from django.urls import path
from family.views import prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', prueba, name='prueba')
]
