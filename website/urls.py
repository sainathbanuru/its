from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^news/', views.news, name="news"),
    url(r'^contact/', views.contact, name="contact"),
    #url(r'^redirect/(?P<lat>[0-9]+\.[0-9]+)/(?P<lng>[0-9]+\.[0-9]+)/(?P<page>[a-z]+)', views.redirect, name="redirect"),

    # redirect/lat/lng/page
    url(r'redirect/(?P<lat>\d+\.\d+)/(?P<lng>\d+\.\d+)/(?P<page>\w+)/', views.redirect, name="redirect"),
    
    #url(r'^redirect', views.redirect, name="redirect"),
    url(r'^temperature/', views.temperature, name="temperature"),
    url(r'^humidity/', views.humidity, name="humidity"),
    url(r'^co2/', views.co2, name="co2"),
    url(r'^smoke/', views.smoke, name="smoke"),
    url(r'^insert/', views.insert.as_view(), name="insert"),
    url(r'^login/', views.login_user.as_view(), name="login"),
    url(r'^logout/', views.logout_user, name="logout"),
]