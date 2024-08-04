from django.urls import path
from tutorial_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/',views.form, name='form')
]
