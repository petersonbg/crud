from django.db import models
from datetime import datetime
from alunos.models import Aluno
from livros.models import Livro
from django.utils.timezone import timezone


class Aluguel(models.Model):
    STATUS_CHOICES = (
        ("E", "Entregue"),
        ("A", "Alugado"),
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    livro = models.ManyToManyField(Livro)
    data_aluguel = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False, blank=False)

    def __str__(self):
        return str(self.aluno)
