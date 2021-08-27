from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name="index"),
    path('pates/', views.page2, name="pates"),
    path('salades/', views.page3, name="salades"),


]

