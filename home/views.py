from django.shortcuts import render, redirect
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.http import HttpResponse


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the contact-us page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'name': form.cleaned_data['name'], 
            'email': form.cleaned_data['email'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'ukkpower@gmail.com', ['ukkpower@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('contact'))
      
    form = ContactForm() 

    return render(request, 'home/contact-us.html', {'form': form})


def about(request):
    """ A view to return the about-us page """

    return render(request, 'home/about-us.html')


def membership(request):
    """ A view to return the membership page """

    return render(request, 'home/membership.html')
