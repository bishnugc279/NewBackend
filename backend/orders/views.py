from django.shortcuts import render, redirect  
from orders.models import Order
from orders.forms import OrderForm

# Create your views here.

def orders_list(request):  
    orders = Order.objects.all()  
    return render(request,'',{'orders':orders})

def create_order(request):  
    if request.method == "POST":  
        form = OrderForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit(request, id):  
    order = Order.objects.get(id=id)  
    return render(request,'',{'order':order})

def update_order(request, id):  
    order = Order.objects.get(id=id)  
    form = OrderForm(request.POST, instance = order)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'order': order})  

def delete_order(request, id):  
    order = Order.objects.get(id=id)  
    order.delete()  
    return redirect('') 

