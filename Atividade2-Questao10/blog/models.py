from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()
    data_publicacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo