from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista, name="lista"),
    path("item/<int:pk>/alternar/", views.alternar, name="alternar"),
    path("item/<int:pk>/excluir/", views.excluir, name="excluir"),
    path("limpar-comprados/", views.limpar_comprados, name="limpar_comprados"),
    path("categorias/", views.categorias, name="categorias"),
    path("categoria/<int:pk>/excluir/", views.excluir_categoria, name="excluir_categoria"),

]