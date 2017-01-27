from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^news/', views.news, name="news"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^redirect/', views.redirect, name="redirect"),
    url(r'^temperature/', views.temperature, name="temperature"),
    url(r'^humidity/', views.humidity, name="humidity"),
    url(r'^co2/', views.co2, name="co2"),
    url(r'^smoke/', views.smoke, name="smoke"),
]