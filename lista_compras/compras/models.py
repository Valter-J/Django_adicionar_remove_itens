from django.db import models


class Categoria(models.Model):
    nome = models.CharField("nome", max_length=50, unique=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome


class Item(models.Model):
    nome = models.CharField("item", max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    comprado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="itens",
    )