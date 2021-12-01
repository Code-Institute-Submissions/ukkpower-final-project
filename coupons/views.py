from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Coupon
from django.contrib.auth.decorators import login_required
from .forms import CouponForm
from django.contrib import messages

@login_required
def add_coupon(request):
    """ Add a coupon to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CouponForm(request.POST, request.FILES)
        if form.is_valid():
            coupon_data = form.save()
            messages.success(request, 'Successfully added coupon!')
            return redirect(reverse('view_coupons'))
        else:
            messages.error(request, 'Failed to add coupon. Please ensure the form is valid.')
    else:
        form = CouponForm()
        
    template = 'add_coupon.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def view_coupons(request):
    """ View coupons """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    coupons_data = Coupon.objects.all()

    context = {
        'coupons': coupons_data,
    }

    return render(request, 'view_coupons.html', context)

@login_required
def edit_coupon(request, coupon_id):
    """ Edit a coupon in the admin """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    coupon_data = get_object_or_404(Coupon, pk=coupon_id)
    if request.method == 'POST':
        form = CouponForm(request.POST, request.FILES, instance=coupon_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated coupon!')
            return redirect(reverse('view_coupons'))
        else:
            messages.error(request, 'Failed to update coupon. Please ensure the form is valid.')
    else:
        form = CouponForm(instance=coupon_data)

    template = 'edit_coupon.html'
    context = {
        'form': form,
        'coupon': coupon_data,
    }

    return render(request, template, context)

@login_required
def delete_coupon(request, coupon_id):
    """ Delete a coupon from the admin """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted area')
        return redirect(reverse('home'))

    coupon_data = get_object_or_404(Coupon, pk=trainer_id)
    coupon_data.delete()
    messages.success(request, 'Coupon deleted!')
    return redirect(reverse('view_coupons'))
