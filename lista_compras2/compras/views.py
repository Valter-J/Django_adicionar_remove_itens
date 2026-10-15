from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ItemForm
from .models import Item


def lista(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            messages.success(request, f"{item.nome} adicionado à lista.")
            return redirect("lista")
    else:
        form = ItemForm()

    itens = Item.objects.all()
    pendentes = itens.filter(comprado=False).count()

    return render(request, "compras/lista.html", {
        "form": form,
        "itens": itens,
        "pendentes": pendentes,
        "tem_comprados": itens.filter(comprado=True).exists(),
    })


@require_POST
def alternar(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.comprado = not item.comprado
    item.save()
    return redirect("lista")


@require_POST
def excluir(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    messages.info(request, f"{item.nome} removido da lista.")
    return redirect("lista")


@require_POST
def limpar_comprados(request):
    total, _ = Item.objects.filter(comprado=True).delete()
    messages.info(request, f"{total} item(ns) comprado(s) removido(s).")
    return redirect("lista")

