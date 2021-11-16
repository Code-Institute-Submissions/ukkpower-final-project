from django.shortcuts import get_object_or_404
from classes.models import GymClass


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    item_total = 0
    quantity = 0

    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            gym_class = get_object_or_404(GymClass, pk=item_id)
            total += item_data * gym_class.price
            product_count += item_data
            item_total += product_count * gym_class.price
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'item_total': item_total,
                'gym_class': gym_class,
            })
        else:
            gym_class = get_object_or_404(GymClass, pk=item_id)
            total += quantity * gym_class.price
            product_count += quantity
            item_total += product_count * gym_class.price
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'item_total': item_total,
                'gym_class': gym_class,
            })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
