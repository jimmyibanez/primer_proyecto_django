from contextlib import ContextDecorator
from multiprocessing import context
from django.shortcuts import render
from relatives.models import Family

# Create your views here.
def save_relative(request):
    new_relative = Family.objects.create(name = 'Luis Montiel', age= 24, birth="1998-08-03")
    context={
        'new_relative':new_relative
    }
    return render(request, 'new_relative.html', context=context)

def list_relative(request):
    relatives = Family.objects.all()
    context={
        'relatives':relatives
    }
    return render(request, 'list_relative.html', context=context)
