from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm

def checkout(request):

    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('timetable'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
