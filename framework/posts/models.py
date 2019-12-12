from django.db import models
from django.utils import timezone

# Create your models here.

class Postagem(models.Model):
    opcao_tema = [
        ('GAM', 'Games'),
        ('TEC', 'Tecnologia'),
        ('MUS', 'Música')
    ]
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(default=1)
    email = models.CharField(max_length=50)
    tema = models.CharField(max_length=3, choices=opcao_tema)
    ativo = models.BooleanField(default=True)

    def __str__(self):
            return self.nome

class Formulario(models.Model):
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    data_nascimento = models.DateTimeField()
    senha = models.CharField(max_length=32)
    confirmacao_senha = models.CharField(max_length=32)

    def __str__(self):
            return self.nome
