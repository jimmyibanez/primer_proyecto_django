
from django.contrib import admin
from django.urls import path
from relatives.views import save_relative, list_relative
from family.views import prueba


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', prueba, name='prueba'),
    path('save_relative/', save_relative, name='save_relative'),
    path('list_relative/', list_relative, name='list_relative')

]
