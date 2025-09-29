'''Exercício 09
Faça um programa que leia três números e mostre-os em ordem decrescente:'''

'''
lista = []
lista.append(int(input("escreva um numero: ")))
lista.append(int(input("escreva outro numero: ")))
lista.append(int(input("escreva outro numero: ")))
lista.sort()
# lista.reverse()
#listaRev = lista[::-1]
listaRev = list(reversed(lista))
print(listaRev)
'''

num1 = int(input("Escreva um numero: "))
num2 = int(input("Escreva outro numero: "))
num3 = int(input("Escreva outro numero: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 >= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)