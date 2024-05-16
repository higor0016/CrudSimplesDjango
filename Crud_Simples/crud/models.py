from django.db import models

# Create your models here.
class Calcado(models.Model):
    class Meta:
        db_table = 'calcado'
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preço', max_digits=4, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    tamanho = models.IntegerField('Tamanho')
    descricao = models.CharField('Descricao',max_length=100)
    marca = models.CharField('Marca',max_length=100)