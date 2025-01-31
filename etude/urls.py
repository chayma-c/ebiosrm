from django.urls import path
from .views import etude_list, etude_detail, test

urlpatterns = [
    path('', etude_list, name='etude_list'),
    path('<int:etude_id>/', etude_detail, name='etude_detail'),
    path('<int:etude_id>/', etude_detail, name='etude_detail'),
    path('test/', test, name='test12'),
]
