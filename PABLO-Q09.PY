# Exercício Python 09: Crie um programa que leia o peso (em kg) e a altura (em metros)
# de uma pessoa, depois calcule o Índice de Massa Corporal (IMC) e mostre o status de
# acordo com a tabela abaixo:
# • Abaixo de 18.5: Abaixo do Peso
# • Entre 18.5 e 24.9: Peso Normal
# • Entre 25 e 29.9: Sobrepeso
# • Entre 30 e 34.9: Obesidade Grau I
# • Entre 35 e 39.9: Obesidade Grau II (severa)
# • Acima de 40: Obesidade Grau III (mórbida)
peso,altura = 0,0
while peso <= 0:
    peso = float(input("Digite seu peso: "))
while altura <=0:
    altura = float(input("Digite sua altura: "))
imc=peso/(altura*altura)
if imc < 18.5:
    print("Abaixo do Peso")
elif imc <= 24.9 and imc >= 18.5:
    print("Peso Normal")
elif imc <= 29.9 and imc >= 25:
    print('Sobrepeso')
elif imc <= 34.9 and imc >= 30:
    print('Obesidade Grau I')
elif imc <= 39.9 and imc >= 35:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (mórbida)')