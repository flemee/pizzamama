from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza, Pate, Salade, Boisson

# Create your views here.
def index(request):
   pizzas = Pizza.objects.all().order_by('prix')
   pates = Pate.objects.all().order_by('prix')
   salades = Salade.objects.all().order_by('prix')
   boissons = Boisson.objects.all().order_by('prix')
   return render(request, 'menu/index.html', {'pizzas': pizzas, 'pates': pates, 'salades': salades, 'boissons': boissons})

def api_get_pizzas(request):
   pizzas = Pizza.objects.all().order_by('prix')
   json = serializers.serialize("json", pizzas)
   return HttpResponse(json)
