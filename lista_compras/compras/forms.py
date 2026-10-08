from django import forms

from .models import Categoria, Item


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Ex.: Hortifrúti", "autofocus": True}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["nome", "quantidade", "categoria"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Ex.: Arroz", "autofocus": True}),
            "quantidade": forms.NumberInput(attrs={"min": 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].empty_label = "Sem categoria"