from django import forms
from .models import ItemInfo
from .models import Comment

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemInfo
        fields = ['name', 'description']
        
class AddItemForm(forms.ModelForm):
    class Meta:
        model = ItemInfo
        fields = ['name', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
