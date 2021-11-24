from django.shortcuts import render, redirect  
from reviews.models import Review
from reviews.forms import ReviewForm

# Create your views here.

def review_list(request):  
    reviews = Review.objects.all()  
    return render(request,'',{'reviews':reviews})

def create_review(request):  
    if request.method == "POST":  
        form = ReviewForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit(request, id):  
    reviews = Review.objects.get(id=id)  
    return render(request,'',{'reviews':reviews})

def update_review(request, id):  
    review = Review.objects.get(id=id)  
    form = ReviewForm(request.POST, instance = review)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'review': review})  

def delete_review(request, id):  
    review = Review.objects.get(id=id)  
    review.delete()  
    return redirect('') 

