from django.shortcuts import render, redirect  
from bookings.models import Booking
from bookings.forms import BookingForm

# Create your views here.

def bookings_list(request):  
    bookings = Booking.objects.all()  
    return render(request,'',{'bookings':bookings})

def create_booking(request):  
    if request.method == "POST":  
        form = BookingForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_booking(request, id):  
    bookings = Booking.objects.get(id=id)  
    return render(request,'',{'bookings':bookings})

def update_booking(request, id):  
    booking = Booking.objects.get(id=id)  
    form = BookingForm(request.POST, instance = booking)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'booking': booking})  

def delete_booking(request, id):  
    booking = Booking.objects.get(id=id)  
    booking.delete()  
    return redirect('') 

