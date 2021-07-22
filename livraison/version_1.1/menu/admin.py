from django.contrib import admin
from .models import Pizza

#affichage dans le panneau d'admin des infos sur les pizzas + abrre de recherche
# .
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom', 'ingredient', 'vegetarienne', 'prix']

# Register your models here.
admin.site.register(Pizza, PizzaAdmin)