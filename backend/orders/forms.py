from django import forms  
from .models import Order  


class OrderForm(forms.ModelForm):  
    class Meta:  
        model = Order  
        fields = (
            'order_id',
            'order_entry_date',
            'order_demand_date',
            'order_item',
            'user_email',
            'operator'
        ) 