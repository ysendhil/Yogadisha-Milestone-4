from django import forms
from .models import ItemInfo

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemInfo
        fields = ['name', 'description']
class AddItemForm(forms.ModelForm):
    class Meta:
        model = ItemInfo
        fields = ['name', 'description']
