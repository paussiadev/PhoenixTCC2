from django.db import models


class Tecido(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cor = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome
