from django import forms
from .models import MenuCategory, MenuDetail, Menu

class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = (
            'category_id',
            'category_name'
            )


class MenuDetailForm(forms.ModelForm):
    class Meta:
        model = MenuDetail
        fields = (
            'menuDetail_id',
            'category_id',
            'item'
            )


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = (
            'menu_id',
            'category_id',
            'menu_name',
            'price',
            'description',
            'booking_option',
            'image'
            )