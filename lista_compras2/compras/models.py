from django.db import models


class Item(models.Model):
    nome = models.CharField("item", max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    comprado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["comprado", "-criado_em"]
        verbose_name = "item"
        verbose_name_plural = "itens"

    def __str__(self):
        return f"{self.quantidade}x {self.nome}"