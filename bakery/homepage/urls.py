from django.urls import path
from . import views


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('story', views.story.as_view(), name='story'),
    path('contact', views.contact.as_view(), name='contact'),
    path('bread', views.bread.as_view(), name='bread'),
    path('drink', views.drink.as_view(), name='drink'),
    path('cookie', views.cookie.as_view(), name='cookie'),
    path('pastry', views.pastry.as_view(), name='pastry'),
    path('cake', views.cake.as_view(), name='cake'),
]