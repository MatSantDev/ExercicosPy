'''Exercício 16
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

import math

ladoH = float(input("Quantos metros mede a horizontal da parede: "))
ladoV = float(input("Quantos metros mede a vertical da parede: "))
area = ladoH * ladoV
litros = area / 3
latas = math.ceil(litros / 18)
valor = latas * 80
print(f"A parade mede {area}m necessario {latas} latas de tintas a comprar no valor total de R${valor}")