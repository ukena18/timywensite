from .models import TodoList, Item
from django import forms

class CreateListForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ["name"]

class CreateItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = "__all__"


