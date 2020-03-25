# Third-party app imports
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# project imports
from nucleo.models import Motorista, Veiculo, TerminalVeiculo
from nucleo.serializer import (
    MotoristaSerializer, VeiculoSerializer,
    TerminalVeiculoSerializer
)


# Create your views here.
class MotoristaList(ModelViewSet):

    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    http_method_names = ['get', 'post']


class VeiculoList(ModelViewSet):

    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    http_method_names = ['get', 'post']


class TerminalVeiculoList(ModelViewSet):

    queryset = TerminalVeiculo.objects.all()
    serializer_class = TerminalVeiculoSerializer
    http_method_names = ['get', 'post']
