from django.db import models
from arriamentos.models import Arriamento
from roupas.models import Roupa
from tamanhos.models import Tamanho
from tecidos.models import Tecido

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    roupa = models.ForeignKey(Roupa, on_delete = models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    tecido = models.ManyToManyField(Tecido, related_name='tecidos')
    arriamento = models.ManyToManyField(Arriamento, related_name='arriamento')
    detalhamento = models.TextField()

    def __str__(self):
        return self.nome