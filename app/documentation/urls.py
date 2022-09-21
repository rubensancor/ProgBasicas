from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:rama_name>/', views.rama_documentation, name='documentation'),
]
