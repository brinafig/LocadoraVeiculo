from model.locacao import *
from model.veiculo import *
from model.VeiculoFactory import *
from datetime import date


print("\n *******Teste*******")

veiculo1 = VeiculoFactory.criar_veiculo("carro", "ABC1234", 150, Categoria.ECONOMICO) 
veiculo2 = VeiculoFactory.criar_veiculo("motorhome", "XYZ9999", 200, Categoria.EXECUTIVO)

print(type(veiculo1))
print(type(veiculo2))

print("\n***** Cálculo com vários dias ******")

loc1 = Locacao(veiculo1, date(2026,3,1), date(2026,3,3))

print(loc1.calcular_valor_locacao())   


print("\n****** Devolução no mesmo dia ******")

loc2 = Locacao(veiculo1, date(2026,3,5), date(2026,3,5))

print(loc2.calcular_valor_locacao())   


print("\n****** Inválido na factory ********")

try:
    VeiculoFactory.criar_veiculo("moto","DEF1234",100,Categoria.ECONOMICO)
except Exception as e:
    print("Erro:", e)


print("\n***** Datas inválidas ******")

try:
    loc3 = Locacao(veiculo1,date(2026,3,10),date(2026,3,5))
    loc3.calcular_valor_locacao()
except Exception as e:
    print("Erro:", e)

print("\n--- TESTANDO O PADRÃO STATE RESTRITIVO ---")
carro_estado = VeiculoFactory.criar_veiculo(tipo="carro", placa="HJI3K45", taxa_diaria=100.0, categoria=Categoria.ECONOMICO)

# 1. Tentar alugar um carro de frota normal
carro_estado.tentar_alugar() # OK - Transitará

# 2. Tentar locar novamente para outro!
carro_estado.tentar_alugar() # Erro Interativo ("Já está alugado!")

# 3. Tentar mandar pra manutenção com cleinte
carro_estado.reter_na_frota_pra_conserto() # Bloqueado

# 4. Devolver 
carro_estado.tentar_devolver() # Ok (Retorna)

# 5. Colocar em checkups da empresa
carro_estado.reter_na_frota_pra_conserto() # Ok 
carro_estado.tentar_alugar() # Falha! Está em Manutenção.