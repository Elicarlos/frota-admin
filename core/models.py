from datetime import date
from django.db import models

# Create your models here.

class Base(models.Model):
    criado = models.DateField('Criedo em', auto_now_add=True)
    modificado  = models.DateField('Modificado em', auto_now=True)
    ativo = models.BooleanField("Ativo ? ", default=True)

    class Meta:
        abstract = True


class TipoVeiculo(Base):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo


class Veiculo(Base):
    STATUS_VEICULO = (
        ('Disponivel', 'Disponivel'),
        ('Indisponível', 'Indisponivel'),
        ('Manutencão', 'Manuntencao')
    )

    descricao = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoVeiculo, on_delete=models.PROTECT )
    placa = models.CharField(max_length=50)
    hodometro_inicial = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_VEICULO, blank=False, null=False, default=1 )

    def __str__(self):
        return f' {self.placa} - {self.status}'
    

class TipoDespesa(Base):
    descricao = models.CharField('Descrição', max_length=100)
    def __str__(self):
        return f' {self.descricao}'
    

class Despesa(Base):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoDespesa, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField('Descrição', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['descricao']
        verbose_name = 'despesa'
        verbose_name_plural = 'despesas'

    def __str__(self):
        return self.descricao


class RegistroSaida(Base):
    placa = models.ForeignKey(Veiculo, related_name='veiculo_registro', verbose_name='Placa', on_delete=models.CASCADE, default=1)
    destino = models.CharField(max_length=100, default="Teresina")
    observacoes = models.TextField(default='Defauet')
    hodometro_inicial = models.IntegerField(default=2)


    def __str__(self) -> str:
        return f"Placa: {self.placa} Destino: {self.destino}"


