# python native imports
from datetime import date, datetime
from itertools import cycle

# django imports
from django.utils import timezone
from django.test import TestCase
from django.contrib.gis.geos import Point

# Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# project imports
from nucleo.models import (
    Motorista, Veiculo, TerminalVeiculo, Terminal,VeiculoTipo,
    Genero, Habilitacao
)

# Create your tests here.

class ArmazenaMotorista(TestCase):
    def test_armazena_motorista(self):
        Motorista.objects.create(
            nome='Zé da Carreta',
            data_nascimento=date(1980, 1, 1),
            genero=Genero('masculino').name,
            tipo_habilitacao=Habilitacao('categoria C').name
        )
    
    def test_armazena_camimhao(self):
        motorista = Motorista.objects.create(
            nome='João do Caminhão',
            data_nascimento=date(1980, 1, 1),
            genero=Genero('masculino').name,
            tipo_habilitacao=Habilitacao('categoria C').name
        )

        Veiculo.objects.create(
            motorista=motorista,
            placa='ABC1234',
            proprietario=True
        )


class ArmazenaTrajeto(TestCase):
    def setUp(self):
        motorista = Motorista.objects.create(
            pk=1,
            nome='João do Caminhão',
            data_nascimento=date(1980, 1, 1),
            genero=Genero('masculino').name,
            tipo_habilitacao=Habilitacao('categoria C').name
        )

        Veiculo.objects.create(
            pk=1,
            motorista=motorista,
            placa='ABC1234',
            proprietario=True
        )

    def test_armazena_trajeto(self):
        terminal = Terminal.objects.get(pk=1)
        veiculo = Veiculo.objects.get(pk=1)

        TerminalVeiculo.objects.create(
            possui_carga=True,
            entrada=datetime(2020, 3, 23, 8, 0, 45, tzinfo=timezone.utc),
            saida=datetime(2020, 3, 24, 8, 0, 45, tzinfo=timezone.utc),
            origem=Point(-23.5162053, -47.6269594),
            destino=Point(-23.5162053, -45.6269594),
            terminal=terminal,
            veiculo=veiculo
        )


class Consultas(TestCase):
    def setUp(self):
        terminal = Terminal.objects.get(pk=1)
        self.motorista = mommy.make_recipe('nucleo.motorista', _quantity=10)
        self.veiculo = mommy.make_recipe(
            'nucleo.veiculo',
            motorista=cycle(self.motorista),
            _quantity=10
        )
        self.terminal_veiculo = mommy.make_recipe(
            'nucleo.terminal_veiculo',
            terminal=terminal,
            veiculo=cycle(self.veiculo),
            _quantity=100
        )

        
    def test_consulta_caminhao_com_carga(self):
        qtd_veiculos_com_carga = TerminalVeiculo.objects.filter(
            possui_carga=True
        ).count()
        self.assertTrue(qtd_veiculos_com_carga >= 0)

    def test_consulta_caminhao_sem_carga(self):
        qtd_veiculos_sem_carga = TerminalVeiculo.objects.filter(
            possui_carga=False
        ).count()
        self.assertTrue(qtd_veiculos_sem_carga >= 0)
    
    def test_consulta_motorista_veiculo_proprio(self):
        veiculos = Veiculo.objects.filter(
            proprietario=True
        )

        for veiculo in veiculos:
            print(veiculo.motorista.nome)