from django.db import models


class Endereco(models.Model):
    ESTADOS_CHOICES = [
        ['AC', 'Acre'],
        ['AL', 'Alagoas'],
        ['AP', 'Amapá'],
        ['AM', 'Amazonas'],
        ['BA', 'Bahia'],
        ['CE', 'Ceará'],
        ['ES', 'Espírito Santo'],
        ['GO', 'Goiás'],
        ['MA', 'Maranhão'],
        ['MT', 'Mato Grosso'],
        ['MS', 'Mato Grosso do Sul'],
        ['MG', 'Minas Gerais'],
        ['PA', 'Pará'],
        ['PB', 'Paraíba'],
        ['PR', 'Paraná'],
        ['PE', 'Pernambuco'],
        ['PI', 'Piauí'],
        ['RJ', 'Rio de Janeiro'],
        ['RN', 'Rio Grande do Norte'],
        ['RS', 'Rio Grande do Sul'],
        ['RO', 'Rondônia'],
        ['RR', 'Roraima'],
        ['SC', 'Santa Catarina'],
        ['SP', 'São Paulo'],
        ['SE', 'Sergipe'],
        ['TO', 'Tocantins'],
        ['DF', 'Distrito Federal'],
    ]
    rua = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.rua

class Aluno(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    ra = models.CharField(max_length=20, null=False, blank=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

