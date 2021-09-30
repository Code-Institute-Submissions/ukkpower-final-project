from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import GymClass, Trainer


def gym_classes(request):
    """ A view to return the index page """

    gym_classes = GymClass.objects.all()

    context = {
        'gym_classes': gym_classes,
    }

    return render(request, 'classes/classes.html', context)


def trainers(request):
    """ A view to return the index page """

    trainers = Trainer.objects.all()

    context = {
        'trainers': trainers,
    }

    return render(request, 'trainers/trainers.html', context)


def trainer(request, trainer_id):
    """ A view to show individual product details """

    trainer = get_object_or_404(Trainer, pk=trainer_id)

    context = {
        'trainer': trainer,
    }

    return render(request, 'trainers/trainer.html', context)
