from django.conf import settings
from django.shortcuts import get_object_or_404
from classes.models import GymClass


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
  
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
