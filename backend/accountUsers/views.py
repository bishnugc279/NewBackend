from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomerUser, SystemUser, ClientUser, User
from .forms import CustomerUserRegisterForm, SystemUserRegisterForm, ClientUserRegisterForm


# Create your views here.
def register(request):
    return render(request, '')

class customerUser_registration(CreateView):
    model = CustomerUser
    form_class = CustomerUserRegisterForm
    template_name = ''


class systemUser_registration(CreateView):
    model = SystemUser
    form_class = SystemUserRegisterForm
    template_name = ''


class clientUser_registration(CreateView):
    model = ClientUser
    form_class = ClientUserRegisterForm
    template_name = ''
