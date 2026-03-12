from .veiculo import Carro, Motorhome

class VeiculoFactory:

    @staticmethod
    def criar_veiculo(tipo, placa, taxa_diaria, categoria):

        tipo = tipo.lower()

        if tipo == "carro":
            return Carro(placa, taxa_diaria, categoria)

        elif tipo == "motorhome":
            return Motorhome(placa, taxa_diaria, categoria)

        else:
            raise ValueError("Tipo de veículo inválido")