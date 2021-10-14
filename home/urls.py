from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact-us', views.contact, name='contact-us'),
    path('about-us', views.about, name='about-us'),
    path('membership', views.membership, name='membership')
]
