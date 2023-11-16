# Exercício Python 11: Escreva um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome “SANTO”.
nome_cidade = str(input("Digite o primeiro nome da cidade: "))
nome_cidade.lower
santo = "santo"
if santo in nome_cidade:
    print(f"A cidade {nome_cidade} tem 'Santo' no nome.")
else: 
    print(f"A cidade {nome_cidade} não tem 'Santo' no nome")