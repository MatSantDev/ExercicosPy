'''Exercício 08
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:'''

produto1 = input("Qual o nome do 1º produto: ")
valor1 = int(input("Escreva o valor: "))
produto2 = input("Qual o nome do 2º produto: ")
valor2 = int(input("Escreva outro numero: "))
produto3 = input("Qual o nome do 3º produto: ")
valor3 = int(input("Escreva outro numero: "))

menorValor = valor1
menor = produto1
if valor2 < menorValor:
    menorValor = valor2
    menor = produto2
if valor3 < menorValor:
    menorValor = valor3
    menor = produto3

print(f"Escolha o produto {menor} que tem o preço R${menorValor} de menor valor")