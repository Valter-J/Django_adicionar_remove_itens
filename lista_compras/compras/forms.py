from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["nome", "quantidade"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Ex.: Arroz", "autofocus": True}),
            "quantidade": forms.NumberInput(attrs={"min": 1}),
        }