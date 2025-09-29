'''Exercício 04
Faça um programa que peça as 4 notas bimestrais e mostre a média.'''

numero1 = int(input("Escreva sua notra do 1º Bimestre: "))
numero2 = int(input("Escreva sua notra do 2º Bimestre: "))
numero3 = int(input("Escreva sua notra do 3º Bimestre: "))
numero4 = int(input("Escreva sua notra do 4º Bimestre: "))

media = (numero1 + numero2 + numero3 + numero4)/4
print(f"Sua média das notas é {media}")
