# Third-party app imports
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# project imports
from nucleo.models import Motorista
from nucleo.serializer import MotoristaSerializer


# Create your views here.
class MotoristaList(ModelViewSet):

    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
