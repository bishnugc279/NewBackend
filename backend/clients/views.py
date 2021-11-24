from django.shortcuts import render, redirect  
from clients.models import BusinessType, BusinessOwner, Client
from clients.forms import BusinessTypeForm, BusinessOwnerForm, ClientForm

# Create your views here.
#business type CURD
def types_list(request):  
    btypes = BusinessType.objects.all()  
    return render(request,'',{'btypes':btypes})

def create_types(request):  
    if request.method == "POST":  
        form = BusinessTypeForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_types(request, id):  
    btype = BusinessType.objects.get(id=id)  
    return render(request,'',{'btype':btype})

def update_type(request, id):  
    btype = BusinessType.objects.get(id=id)  
    form = BusinessTypeForm(request.POST, instance = btype)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'btype': btype})  

def delete_type(request, id):  
    btype = BusinessType.objects.get(id=id)  
    btype.delete()  
    return redirect('') 


# next
# Business owner CURD
def owners_list(request):  
    owners = BusinessOwner.objects.all()  
    return render(request,'',{'owners':owners})

def create_owners(request):  
    if request.method == "POST":  
        form = BusinessOwnerForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_owners(request, id):  
    owner = BusinessOwner.objects.get(id=id)  
    return render(request,'',{'owner':owner})

def update_owner(request, id):  
    owner = BusinessOwner.objects.get(id=id)  
    form = BusinessOwnerForm(request.POST, instance = owner)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'owner': owner})  

def delete_owner(request, id):  
    owner = BusinessOwner.objects.get(id=id)  
    owner.delete()  
    return redirect('') 


# next
# Business owner CURD
def clients_list(request):  
    clients = Client.objects.all()  
    return render(request,'',{'clients':clients})

def create_clients(request):  
    if request.method == "POST":  
        form = ClientForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_clients(request, id):  
    client = Client.objects.get(id=id)  
    return render(request,'',{'client':client})

def update_client(request, id):  
    client = Client.objects.get(id=id)  
    form = ClientForm(request.POST, instance = client)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'client': client})  

def delete_client(request, id):  
    client = Client.objects.get(id=id)  
    client.delete()  
    return redirect('') 

