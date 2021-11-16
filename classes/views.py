from django.shortcuts import render, get_object_or_404
from .models import GymClass, Trainer, Timetable


def gym_classes(request):
    """ A view to return the index page """

    gym_classes_data = GymClass.objects.all()

    context = {
        'gym_classes': gym_classes_data,
    }

    return render(request, 'classes/classes.html', context)


def gym_class(request, class_id):
    """ A view to show individual product details """

    gym_class_data = get_object_or_404(GymClass, pk=class_id)
    trainers_data = gym_class_data.trainer.all()
    timetables = Timetable.objects.select_related().filter(gym_class=class_id)

    context = {
        'gym_class': gym_class_data,
        'trainers': trainers_data,
        'timetables': timetables
    }

    return render(request, 'classes/class.html', context)


def timetable(request):
    """ A view to return the index page """

    timetable_entries = Timetable.objects.all()

    context = {
        'timetable_entries': timetable_entries,
    }

    return render(request, 'classes/timetable.html', context)


def trainers(request):
    """ A view to return the index page """

    trainers_data = Trainer.objects.all()

    context = {
        'trainers': trainers_data,
    }

    return render(request, 'trainers/trainers.html', context)


def trainer(request, trainer_id):
    """ A view to show individual product details """

    trainer_data = get_object_or_404(Trainer, pk=trainer_id)

    context = {
        'trainer': trainer_data,
    }

    return render(request, 'trainers/trainer.html', context)
