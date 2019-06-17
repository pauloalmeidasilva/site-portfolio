from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class conhecimento(models.Model):
    nome = models.CharField(max_length=200)
    tempo = models.CharField(max_length=200)
    classificacao = models.IntegerField()

    def __str__(self):
        return self.nome

class formacao(models.Model):
    curso = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.CharField(max_length=4)
    data_fim = models.CharField(max_length=5)

    def __str__(self):
        return self.curso

class experiencia(models.Model):
    cargo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.CharField(max_length=4)
    data_fim = models.CharField(max_length=5)

    def __str__(self):
        return self.cargo

class portfolio(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    descricao = models.TextField(blank=False)
    url = models.CharField(max_length=200, blank=True)
    foto = models.FileField(upload_to='%Y/%m/%d/')
    linguagem = models.CharField(max_length=200)

    def __str__(self):
        return self.nome