from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.index, name='home'),
    # path('about',views.aboutme, name='aboutme'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
]
