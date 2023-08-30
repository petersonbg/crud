from django.db import models

class Categorias(models.Model):
    categoria = models.CharField(max_length=50,
                                 null=False,
                                 blank=False)

    def __str__(self):
        return self.categoria


class Livro(models.Model):
    titulo = models.CharField(max_length=50,
                              null=False,
                              blank=False)
    autor = models.CharField(max_length=50,
                             null=False,
                             blank=False)
    editora = models.CharField(max_length=50,
                               null=False,
                               blank=False)
    descricao = models.TextField(max_length=255)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
