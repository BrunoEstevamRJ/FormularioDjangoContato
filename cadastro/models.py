from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.DecimalField(max_digits=15, decimal_places=2)
    email = models.EmailField()
    menssagem = models.TextField(max_length=255)

    def __str__(self):
        return self.nome
