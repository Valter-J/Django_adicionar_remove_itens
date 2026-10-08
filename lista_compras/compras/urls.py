from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista, name="lista"),
    path("item/<int:pk>/alternar/", views.alternar, name="alternar"),
    path("item/<int:pk>/excluir/", views.excluir, name="excluir"),
]