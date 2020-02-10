from django.urls import path

from . import views

app_name ='photostyle'
urlpatterns = [
    path('', views.select, name='select'),
    path('generate/', views.generate, name='generate'),
]