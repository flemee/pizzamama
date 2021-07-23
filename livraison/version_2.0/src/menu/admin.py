from django.contrib import admin
from .models import Pizza
from .models import Pate
from .models import Salade
from .models import Boisson

# affichage dans le panneau d'admin des infos sur les pizzas + abre de recherche

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom', 'ingredient', 'vegetarienne', 'prix']


class PateAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom', 'ingredient', 'vegetarienne', 'prix']

class SaladeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix')
    search_fields = ['nom', 'ingredient', 'prix']

class BoissonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ['nom', 'prix']


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pate, PateAdmin)
admin.site.register(Salade, SaladeAdmin)
admin.site.register(Boisson, BoissonAdmin)