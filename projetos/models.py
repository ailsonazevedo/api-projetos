from django.db import models
from uuid import uuid4

# Create your models here.


def upload_imagem_projeto(instance, filename):
    return f"{instance.id_projeto}-{filename}"

class Projetos(models.Model):
    id_projeto = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField('Nome do projeto',max_length=250)
    descricao = models.CharField('Descriação do projeto', max_length=300)
    dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default = False)
    imagem = models.ImageField(upload_to=upload_imagem_projeto, blank=True, null=True)


    def __str__(self):
        return str(self.nome)