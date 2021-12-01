from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib import messages

from classes.models import GymClass
from coupons.models import Coupon


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    gym_class = get_object_or_404(GymClass, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = quantity
        messages.success(
            request, f"Updated {gym_class.name} quantity to {cart[item_id]}"
        )
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {gym_class.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Adjust the quantity of the gym class to the specified amount"""

    gym_class = get_object_or_404(GymClass, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f"Updated {gym_class.name} quantity to {cart[item_id]}"
        )
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {gym_class.name} from your cart')
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_cart_item(request, item_id):
    """Remove the item from the cart"""

    try:
        cart = request.session.get('cart', {})
        name = request.POST['item_name']

        cart.pop(item_id)
        messages.success(request, f'Removed {name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_discount(request):
    # If coupon submitted, check if exists, active and valid period
    if request.POST['coupon_code']:
        coupon = Coupon.objects.filter(
            code=request.POST['coupon_code']).first()
        if not coupon:
            messages.error(request, 'No such coupon found')
        else:
            if coupon.active:
                cart = request.session.get('cart', {})
                cart['discount'] = coupon.discount
                request.session['cart'] = cart
                messages.success(request, 'Coupon added')
            else:
                messages.error(request, 'Coupon no longer active')
    else:
        messages.error(request, 'No coupon submitted')

    return redirect(reverse('view_cart'))
