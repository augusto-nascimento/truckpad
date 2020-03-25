# Third-party app imports
from rest_framework.serializers import ModelSerializer

# project imports
from nucleo.models import Motorista, Veiculo, TerminalVeiculo


class MotoristaSerializer(ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['id', 'nome', 'data_nascimento', 'genero', 'tipo_habilitacao']


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'motorista', 'placa', 'proprietario']


class TerminalVeiculoSerializer(ModelSerializer):
    class Meta:
        model = TerminalVeiculo
        fields = ['id', 'possui_carga', 'entrada', 'saida', 'terminal', 'veiculo']
