'''Exercício 22
Faça um programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).'''

num = int(input("Escreva um numero inteiro: "))
if(num % 2 == 0):
    print("O numero é par")
else:
    print("O numero é impar")