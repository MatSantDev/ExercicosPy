'''Exercício 01
Faça um programa que peça dois números e imprima o maior deles.'''

num1 = int(input("Escreva um numero: "))
num2 = int(input("Escreva outro numero: "))

if(num1 > num2):
    print(f"O numero maior é {num1} e o menor é {num2}")
elif(num2 > num1):
    print(f"O numero maior é {num2} e o menor é {num1}")
else:
    print(f"Os numero são iguais")