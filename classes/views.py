from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import GymClass, Trainer, Timetable
from django.contrib.auth.decorators import login_required
from .forms import ClassForm, TrainerForm, TimetableForm
from django.contrib import messages


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


@login_required
def add_class(request):
    """ Add a class to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added class!')
            return redirect(reverse('view_class'))
        else:
            messages.error(
                request,
                'Failed to add class. Please ensure the form is valid.'
                           )
    else:
        form = ClassForm()

    template = 'classes/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def view_classes(request):
    """ View classes """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    gym_classes_data = GymClass.objects.all()

    context = {
        'gym_classes': gym_classes_data,
    }

    return render(request, 'classes/view_class.html', context)


@login_required
def edit_class(request, class_id):
    """ Edit a class in the admin """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    gym_classes_data = get_object_or_404(GymClass, pk=class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES,
                         instance=gym_classes_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated class!')
            return redirect(reverse('view_class'))
        else:
            messages.error(
                request,
                'Failed to update class. Please ensure the form is valid.'
                )
    else:
        form = ClassForm(instance=gym_classes_data)

    template = 'classes/edit_class.html'
    context = {
        'form': form,
        'gym_class': gym_classes_data,
    }

    return render(request, template, context)


@login_required
def delete_class(request, class_id):
    """ Delete a class from the admin """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    gym_classes_data = get_object_or_404(GymClass, pk=class_id)
    gym_classes_data.delete()
    messages.success(request, 'Class deleted!')
    return redirect(reverse('view_class'))


@login_required
def add_trainer(request):
    """ Add a trainer to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added trainer!')
            return redirect(reverse('view_trainers'))
        else:
            messages.error(
                request,
                'Failed to add trainer. Please ensure the form is valid.'
                )
    else:
        form = TrainerForm()

    template = 'trainers/add_trainer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def view_trainers(request):
    """ View trainers """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    trainers_data = Trainer.objects.all()

    context = {
        'trainers': trainers_data,
    }

    return render(request, 'trainers/view_trainers.html', context)


@login_required
def edit_trainer(request, trainer_id):
    """ Edit a trainer in the admin """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    trainer_data = get_object_or_404(Trainer, pk=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated trainer!')
            return redirect(reverse('view_trainers'))
        else:
            messages.error(
                request,
                'Failed to update trainer. Please ensure the form is valid.')
    else:
        form = TrainerForm(instance=trainer_data)

    template = 'trainers/edit_trainer.html'
    context = {
        'form': form,
        'trainer': trainer_data,
    }

    return render(request, template, context)


@login_required
def delete_trainer(request, trainer_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    trainer_data = get_object_or_404(Trainer, pk=trainer_id)
    trainer_data.delete()
    messages.success(request, 'Trainer deleted!')
    return redirect(reverse('view_trainers'))


@login_required
def add_timetable(request):
    """ Add a timetable to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TimetableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added timetable!')
            return redirect(reverse('view_timetables'))
        else:
            messages.error(
                request,
                'Failed to add timetable. Please ensure the form is valid.')
    else:
        form = TimetableForm()

    template = 'timetables/add_timetable.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def view_timetables(request):
    """ View trainers """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    timetables_data = Timetable.objects.all()

    context = {
        'timetables': timetables_data,
    }

    return render(request, 'timetables/view_timetables.html', context)


@login_required
def edit_timetable(request, timetable_id):
    """ Edit a timetable in the admin """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    timetable_data = get_object_or_404(Timetable, pk=timetable_id)
    if request.method == 'POST':
        form = TimetableForm(request.POST, request.FILES,
                             instance=timetable_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated timetable!')
            return redirect(reverse('view_timetables'))
        else:
            messages.error(
                request,
                'Failed to update timetable. Please ensure the form is valid.'
                )
    else:
        form = TimetableForm(instance=timetable_data)

    template = 'timetables/edit_timetable.html'
    context = {
        'form': form,
        'timetable': timetable_data,
    }

    return render(request, template, context)


@login_required
def delete_timetable(request, timetable_id):
    """ Delete a timetable from the admin """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    timetable_data = get_object_or_404(
        Timetable,
        pk=timetable_id
        )
    timetable_data.delete()
    messages.success(request, 'Timetable deleted!')
    return redirect(reverse('view_timetables'))
