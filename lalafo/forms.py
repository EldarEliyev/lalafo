from django import forms
from.models.comment import Comment
from.models.elan import Elan

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ["comment"]

class ElanForm(forms.ModelForm):
    class Meta:
        model = Elan 
        fields = ["location",  "comment",  "subcategory",  "title",  "description",  "image",  "price",  "discount",  "is_active",  "is_vip",  "is_premium"]

        