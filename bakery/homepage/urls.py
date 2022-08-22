from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('story', views.story, name='story'),
    path('contact', views.contact, name='contact'),
    path('bread', views.bread, name='bread'),
    path('drink', views.drink, name='drink'),
    path('cookie', views.cookie, name='cookie'),
    path('pastry', views.pastry, name='pastry'),
    path('cake', views.cake, name='cake'),
]