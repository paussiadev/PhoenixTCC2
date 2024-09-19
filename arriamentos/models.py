from django.db import models

class Arriamento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cor = models.CharField(max_length=50, null=True)
    tamanho = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.nome