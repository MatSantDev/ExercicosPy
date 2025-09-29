'''Exercício 17
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math

ladoH = float(input("Quantos metros mede a horizontal da parede: "))
ladoV = float(input("Quantos metros mede a vertical da parede: "))

area = ladoH * ladoV
litros = (area / 6) * 1.1
latas = math.ceil(litros / 18)
valorlatas = latas * 80
galoes = math.ceil(litros / 3.6)
valorgaloes = galoes * 25

div = litros // 18
resto = (litros % 18)
div2 = math.ceil(resto / 3.6)
valor = div*80 + div2*25

print(f"Deve comprar {litros:.2f} litros de tintas")
print(f"Deve comprar {latas} latas de tintas se comprar apenas latas no valor total de R${valorlatas:.2f}")
print(f"Deve comprar {galoes} galoes de tintas se comprar apenas galoes no valor total de R${valorgaloes:.2f}")
print(f'Deve comprar {div} latas de tintas e {div2} galoes de tintas para melhor eficiencia no valor total de R${valor:.2f}')