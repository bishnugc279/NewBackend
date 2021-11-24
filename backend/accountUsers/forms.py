from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import CustomerUser, SystemUser, ClientUser, User


class CustomerUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.CharField(required=True)
    phone_number= forms.IntegerField(required=True)
    country = forms.CharField(required=True)
    district = forms.CharField(required=True)
    ward = forms.CharField(required=True)
    address = forms.CharField(required=True)
    dob = forms.DateField(required=True)
    gender = forms.CharField(required=True)
    created_date = forms.DateTimeField(required=True)
    updated_date = forms.DateTimeField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data_get('first_name')
        user.last_name = self.cleaned_data_get('last_name')
        user.email_address = self.cleaned_data_get('email_address')
        user.save()
        customerUser = CustomerUser.objects.create(user=user)
        phone_number = self.cleaned_data_get('phone_number')
        country = self.cleaned_data_get('country')
        district = self.cleaned_data_get('district')
        ward = self.cleaned_data_get('ward')
        address = self.cleaned_data_get('address')
        dob = self.cleaned_data_get('dob')
        gender = self.cleaned_data_get('gender')
        created_date = self.cleaned_data_get('created_date')
        updated_date = self.cleaned_data_get('updated_date')
        customerUser.save()
        return customerUser

        

class SystemUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.CharField(required=True)
    systemuser_gender = forms.CharField(required=True)
    systemuser_phone = forms.CharField(required=True)
    systemuser_mobile = forms.CharField(required=True)
    systemuser_address = forms.CharField(required=True)
    role = forms.CharField(required=True)
    created_date = forms.DateTimeField(required=True)
    updated_date = forms.DateTimeField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data_get('first_name')
        user.last_name = self.cleaned_data_get('last_name')
        user.email_address = self.cleaned_data_get('email_address')
        user.save()
        systemUser = CustomerUser.objects.create(user=user)
        systemuser_gender = self.cleaned_data_get('systemuser_gender')
        systemuser_phone = self.cleaned_data_get('systemuser_phone')
        systemuser_mobile = self.cleaned_data_get('systemuser_mobile')
        systemuser_address = self.cleaned_data_get('systemuser_address')
        role = self.cleaned_data_get('role')
        created_date = self.cleaned_data_get('created_date')
        updated_date = self.cleaned_data_get('updated_date')
        systemUser.save()
        return systemUser



class ClientUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.CharField(required=True)
    client_user_gender = forms.CharField(required=True)
    client_user_phone = forms.CharField(required=True)
    client_user_mobile = forms.CharField(required=True)
    client_user_address = forms.CharField(required=True)
    role = forms.CharField(required=True)
    created_date = forms.DateTimeField(required=True)
    updated_date = forms.DateTimeField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data_get('first_name')
        user.last_name = self.cleaned_data_get('last_name')
        user.email_address = self.cleaned_data_get('email_address')
        user.save()
        clientUser = ClientUser.objects.create(user=user)
        client_user_gender = self.cleaned_data_get('client_user_gender')
        client_user_phone = self.cleaned_data_get('client_user_phone')
        client_user_mobile = self.cleaned_data_get('client_user_mobile')
        client_user_address = self.cleaned_data_get('client_user_address')
        role = self.cleaned_data_get('role')
        created_date = self.cleaned_data_get('created_date')
        updated_date = self.cleaned_data_get('updated_date')
        clientUser.save()
        return clientUser





