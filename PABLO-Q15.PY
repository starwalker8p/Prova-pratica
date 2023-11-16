# EXERCICIO OBRIGATORIO PARA TODOS:Imagine que você está planejando uma viagem de carro e gostaria de calcular o
# quanto de combustível você irá gastar e quanto isso vai custar. O objetivo deste
# exercício é criar um programa que peça ao usuário para inserir:
# 1. A distância total da viagem em quilômetros.
# 2. O consumo médio de combustível do carro (km por litro).
# 3. O preço do combustível por litro.
# O programa deve calcular e exibir:
# • A quantidade estimada de combustível necessária para a viagem.
# • O custo total do combustível.
# Para adicionar mais contexto e desafio ao exercício, considere as seguintes
# variações de preço para o combustível dependendo da região:
# • Região Norte: R$ 5,30 por litro
# • Região Nordeste: R$ 5,10 por litro
# • Região Centro-Oeste: R$ 5,20 por litro
# • Região Sudeste: R$ 5,00 por litro
# • Região Sul: R$ 5,15 por litro
# O usuário deve inserir a região para que o programa calcule o preço com base
# nos valores acima
distancia,km_litro,regiao = 0,0,0
while distancia <= 0:
    distancia = float(input("Digite a distancia da viagem: "))
while km_litro <= 0:
    km_litro = float(input("Quantos litros de combustivel seu carro consome em um km? : "))
regioes = ['sudeste','nordeste','sul','centro','norte']
preço = [5.00,5.10,5.15,5.20,5.30]
while regiao not in regioes:
    regiao = str(input("Qual sua regiao?")).replace(' ','').lower()
indice=regioes.index(regiao)
print(f"quantidade de combustivel necessaria: {distancia/km_litro}L")
print(f"Custo do combustivo necessario para a viagem: R${(distancia/km_litro)*preço[indice]}")
