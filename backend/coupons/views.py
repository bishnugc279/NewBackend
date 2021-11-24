from django.shortcuts import render, redirect  
from coupons.models import Coupon
from coupons.forms import CouponForm

# Create your views here.

def coupon_list(request):  
    coupons = Coupon.objects.all()  
    return render(request,'',{'coupons':coupons})

def create_coupon(request):  
    if request.method == "POST":  
        form = CouponForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_coupon(request, id):  
    coupons = Coupon.objects.get(id=id)  
    return render(request,'',{'coupons':coupons})

def update_coupon(request, id):  
    coupon = Coupon.objects.get(id=id)  
    form = CouponForm(request.POST, instance = coupon)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'coupon': coupon})  

def delete_coupon(request, id):  
    coupon = Coupon.objects.get(id=id)  
    coupon.delete()  
    return redirect('') 

