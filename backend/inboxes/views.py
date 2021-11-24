from django.shortcuts import render, redirect  
from inboxes.models import Inbox
from inboxes.forms import InboxForm

# Create your views here.

def inbox_list(request):  
    inboxes = Inbox.objects.all()  
    return render(request,'',{'inboxes':inboxes})

def create_inbox(request):  
    if request.method == "POST":  
        form = InboxForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_inbox(request, id):  
    inbox = Inbox.objects.get(id=id)  
    return render(request,'',{'inbox':inbox})

def update_inbox(request, id):  
    inbox = Inbox.objects.get(id=id)  
    form = InboxForm(request.POST, instance = inbox)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'inbox': inbox})  

def delete_inbox(request, id):  
    inbox = Inbox.objects.get(id=id)  
    inbox.delete()  
    return redirect('') 

