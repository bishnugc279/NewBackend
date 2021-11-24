from django import forms
from .models import BusinessType, BusinessOwner, Client

class BusinessTypeForm(forms.ModelForm):
    class Meta:
        model = BusinessType
        fields = (
            'businesstype_id',
            'businesstype_name'
        )

class BusinessOwnerForm(forms.ModelForm):
    class Meta:
        model = BusinessOwner
        fields = (
            'owner_id',
            'owner_first_name',
            'owner_last_name',
            'owner_email',
            'owner_phoneno',
            'owner_mobile',
            'owner_address',
            'owner_gender',
            'joined_date'
        )

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'client_id',
            'client_first_name',
            'client_last_name',
            'pan_number',
            'businesstype_id',
            'owner_id',
            'email_address',
            'landline_number',
            'mobile_number',
            'country',
            'district',
            'ward',
            'address',
            'description',
            'sub_description',
            'number_of_seats',
            'private_rooms',
            'open_hour',
            'closing_hour',
            'price_range',
            'image'
        )