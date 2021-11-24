from django.shortcuts import render, redirect  
from menus.models import MenuCategory, MenuDetail, Menu
from menus.forms import MenuCategoryForm, MenuDetailForm, MenuForm

# Create your views here.
# Menu Category CURD
def category_list(request):  
    category = MenuCategory.objects.all()  
    return render(request,'',{'category':category})

def create_category(request):  
    if request.method == "POST":  
        form = MenuCategoryForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_category(request, id):  
    categories = MenuCategory.objects.get(id=id)  
    return render(request,'',{'categories':categories})

def update_category(request, id):  
    category = MenuCategory.objects.get(id=id)  
    form = MenuCategoryForm(request.POST, instance = category)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'category': category})  

def delete_category(request, id):  
    category = MenuCategory.objects.get(id=id)  
    category.delete()  
    return redirect('') 


# Next
# Menu Detail CURD
def detail_list(request):  
    detail = MenuDetail.objects.all()  
    return render(request,'',{'detail':detail})

def create_detail(request):  
    if request.method == "POST":  
        form = MenuDetailForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_detail(request, id):  
    details = MenuDetail.objects.get(id=id)  
    return render(request,'',{'details':details})

def update_details(request, id):  
    detail = MenuDetail.objects.get(id=id)  
    form = MenuDetailForm(request.POST, instance = detail)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'detail': detail})  

def delete_detail(request, id):  
    detail = MenuDetail.objects.get(id=id)  
    detail.delete()  
    return redirect('') 

# Next
# Menu  CURD
def menu_list(request):  
    menu = Menu.objects.all()  
    return render(request,'',{'menu':menu})

def create_menu(request):  
    if request.method == "POST":  
        form = MenuForm(request.POST)  
        if form.is_valid():   
            form.save()  
            return redirect('')   
        return render(request,'',{'form':form})

def edit_menu(request, id):  
    menus = Menu.objects.get(id=id)  
    return render(request,'',{'menus':menus})

def update_menu(request, id):  
    menu = Menu.objects.get(id=id)  
    form = MenuForm(request.POST, instance = menu)  
    if form.is_valid():  
        form.save()  
        return redirect('')  
    return render(request, '', {'menu': menu})  

def delete_menu(request, id):  
    menu = Menu.objects.get(id=id)  
    menu.delete()  
    return redirect('') 