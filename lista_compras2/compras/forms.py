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
        
        def clean_nome(self):
            nome = self.cleaned_data["nome"].strip()
            if Item.objects.filter(nome__iexact=nome, comprado=False).exists():
                raise forms.ValidationError(f"{nome} já está na lista.")
            return nome


