# Exercício Python 07: Crie um programa que leia o valor de um produto e imprima o
# valor com desconto, tendo em vista que o desconto aplicado é de 10%
valor_produto = 0
while valor_produto <= 0:
    valor_produto = float(input("Digite o valor do produto: "))
print(f"Valor original: {valor_produto}\nValor do desconto: {valor_produto/100*10}\nValor do produto após o desconto: {valor_produto/100*90}")
