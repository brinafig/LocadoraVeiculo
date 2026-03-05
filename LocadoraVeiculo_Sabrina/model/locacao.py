from datetime import date
from .veiculo import Veiculo
from .ExcecoesPersonalizadas import DataInvalidaError


class Locacao:

    def __init__(self, veiculo: Veiculo, data_inicio: date, data_fim: date):
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, obj):
        if obj is not None:
            self.__veiculo = obj
        else:
            raise Exception("Objeto Veículo obrigatório!!!")

    def calcular_valor_locacao(self) -> float:

        if self.data_inicio is None or self.data_fim is None:
            raise DataInvalidaError("Datas inválidas")

        if self.data_fim < self.data_inicio:
            raise DataInvalidaError("Data final não pode ser menor que a data inicial")

        if self.veiculo.taxa_diaria is None or self.veiculo.taxa_diaria <= 0:
            raise ValueError("Taxa diária inválida")

        if not hasattr(self.veiculo, "valor_seguro") or self.veiculo.valor_seguro < 0:
            raise ValueError("Valor do seguro inválido")

        dias = (self.data_fim - self.data_inicio).days

        if dias == 0:
            dias = 1
        else:
            dias = dias + 1

        total = (dias * self.veiculo.taxa_diaria) + self.veiculo.valor_seguro

        return total