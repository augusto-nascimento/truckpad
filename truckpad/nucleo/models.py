from django.db import models
from enum import Enum
from django.core.exceptions import ValidationError
import re
from django.contrib.gis.db.models import PointField

# Create your models here.


def validar_placa(value):
    reg = re.compile(r'[A-Z]{3}\d\w\d{2}')
    if not reg.match(value):
        raise ValidationError(u'%s Formato de placa inválido' % value)


class Genero(Enum):
    m = 'masculino'
    f = 'feminino'
    x = 'outros'


class Habilitacao(Enum):
    B = 'categoria B'
    C = 'categoria C'
    D = 'categoria D'
    E = 'categoria E'


class Motorista(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    data_nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(
        max_length=1,
        choices=[(tag.name, tag.value) for tag in Genero],
        blank=True,
        null=True
    )
    tipo_habilitacao = models.CharField(
        max_length=1,
        choices=[(tag.name, tag.value) for tag in Habilitacao],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    motorista = models.ForeignKey(
        Motorista,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    placa = models.CharField(
        max_length=7,
        db_index=True,
        validators=[validar_placa]
    )
    proprietario = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.placa


class VeiculoTipo(models.Model):
    descricao = models.CharField(max_length=50)


class Terminal(models.Model):
    nome = models.CharField(max_length=50)
    localizacao = PointField()

    def __str__(self):
        return self.nome


class TerminalVeiculo(models.Model):
    possui_carga = models.BooleanField(blank=True, null=True)
    entrada = models.DateTimeField(auto_now_add=True)
    saida = models.DateTimeField(blank=True, null=True)
    origem = PointField()
    destino = PointField()
    terminal = models.ForeignKey(Terminal, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)

    def __str__(self):
        return '%s: %s - %s' % (self.veiculo.placa, self.entrada, self.saida)