from django.db import models

class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class PizzaPersonnalisable(Pizza):

    def __init__(self):
        super().__init__()
pass



class Pate(models.Model):
    nom = models.CharField(max_length=300)
    ingredients = models.CharField(max_length=500)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Salade(models.Model):
    nom = models.CharField(max_length=300)
    ingredients = models.CharField(max_length=500)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Boisson(models.Model):
    nom = models.CharField(max_length=300)
    prix = models.FloatField(default=0)

    def __str__(self):
        return self.nom

