# Third-party app imports
from rest_framework.serializers import ModelSerializer

# project imports
from nucleo.models import Motorista


class MotoristaSerializer(ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['id', 'nome', 'data_nascimento', 'genero', 'tipo_habilitacao']
