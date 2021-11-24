from django import forms
from .models import Coupon

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = (
            'coupon_id',
            'coupon_name',
            'coupon_code',
            'start_date',
            'end_date',
            'create_date',
            'update_date',
            'description',
            'coupon_image',
            'client_id',
            'clientuser_id'
        )