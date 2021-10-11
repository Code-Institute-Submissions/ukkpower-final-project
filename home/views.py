from django.shortcuts import render
from profiles.models import UserProfile
from django.contrib.auth.models import User


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the contact-us page """

    return render(request, 'home/contact-us.html')


def about(request):
    """ A view to return the about-us page """

    return render(request, 'home/about-us.html')
