from django.urls import path 
from . import views
urlpatterns = [
    path ('atelierpart' , views.getAtelierPart)  ,
    path('atelier1' , views.getAtelier01),
    path('valeurmetier' , views.getValeurMetier),
    path('beinsport' , views.getBienSupport),
    path('evenment' , views.getEvenment),
      path ('atelierpart/add' , views.addAtelierPart)  ,
    path('atelier1/add' , views.addAtelier01),
    path('valeurmetier/add' , views.addvaleurmetier),
    path('beinsport/add' , views.addBiensupport),
    path('evenment/add' , views.addEvenment),
]