from django import forms
from .models import Coupon


class CouponForm(forms.ModelForm):

    class Meta:
        model = Coupon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
