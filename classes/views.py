from django.shortcuts import render
from .models import GymClass


def classes(request):
    """ A view to return the index page """

    gym_classes = GymClass.objects.all()

    context = {
        'gym_classes': gym_classes,
    }

    return render(request, 'classes/classes.html', context)
