from django.shortcuts import get_object_or_404
from classes.models import GymClass
import decimal


def cart_contents(request):

    cart_items = []
    sub_total = 0
    total = 0
    product_count = 0
    item_total = 0
    quantity = 0
    discount = 0

    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if item_id == 'discount':
            discount = item_data
        else:
            if isinstance(item_data, int):
                gym_class = get_object_or_404(GymClass, pk=item_id)
                sub_total += item_data * gym_class.price
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
                sub_total += quantity * gym_class.price
                product_count += quantity
                item_total += product_count * gym_class.price
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'item_total': item_total,
                    'gym_class': gym_class,
                })

    if discount > 0:
        total = round(sub_total * decimal.Decimal((1 - discount / 100)), 2)
    else:
        total = sub_total

    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'discount': discount,
        'total': total,
        'product_count': product_count,
    }

    return context
