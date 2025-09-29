'''Exercício 07
Faça um programa que leia três números e mostre o maior e o menor deles:'''

num1 = int(input("Escreva um numero: "))
num2 = int(input("Escreva outro numero: "))
num3 = int(input("Escreva outro numero: "))

'''
lista = [num1, num2, num3]
lista.sort()
print(f"Maior: {lista[-1]} | Meio: {lista[1]} | Menor: {lista[0]}")
'''

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Definindo o menor
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")