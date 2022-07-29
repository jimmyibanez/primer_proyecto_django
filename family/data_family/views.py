from multiprocessing import context
from django.shortcuts import render

from data_family.models import Family
from family.views import relatives

# Create your views here.
def create_relative(request):
    new_relative = Family.objects.create(name = 'Edgar Allan Poe', age= 65)
    context = {
        'new_relative':new_relative
    }
    return render(request, 'new_relative.html', context=context)

def list_relative(request):
    relatives = Family.objects.all()
    context = {
        'relatives' : relatives
    }
    return render(request, 'list_relative.html', context=context)