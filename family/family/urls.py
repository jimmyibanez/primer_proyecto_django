
from django.contrib import admin
from django.urls import path
from data_family.views import list_relative
from family.views import prueba
from data_family.views import create_relative

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/', prueba, name='prueba'),
    path('new_relative/', create_relative, name='create_relative'),
    path('list_relative/', list_relative, name='list_relative')

]
