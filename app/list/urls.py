from django.urls import path

from . import views

name = 'list'

urlpatterns = [
    path('', views.index, name='index')
]