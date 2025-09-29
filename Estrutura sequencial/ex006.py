'''Exercício 06
Faça um programa que peça o raio de um círculo, calcule e mostre sua área:'''
import math

raio = float(input("Qual o raio: "))
area = math.pi * raio**2
print(f"A area de um circulo que tem um raio de {raio} é {area:.3f}")
