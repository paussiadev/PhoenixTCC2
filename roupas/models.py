from typing import Any
from django.db import models

class Roupa(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome