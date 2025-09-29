'''Exercício 11
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.'''

numeroInt1 = int(input("Digite um numero inteiro: "))
numeroInt2 = int(input("Digite outro numero inteiro: "))
numeroFloat = float(input("Digite um numeor real: "))

res1 = (numeroInt1*2)*(numeroInt2/2)
res2 = (numeroInt1*3)+numeroFloat
res3 = numeroFloat**3

print(f"O produto do dobro do primeiro com metade do segun é {res1}")
print(f"A soma do triplo do primeiro com o terceiro é {res2}")
print(f"O terceiro elevado ao cubo é {res3}")