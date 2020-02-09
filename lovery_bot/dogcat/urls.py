from django.urls import path

from . import views

app_name ='dogcat'
urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('dogcat/', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
]