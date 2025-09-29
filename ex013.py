'''Exercício 13
Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

print("Dias da semana")
print("----"*10)
print("1 - Domingo")
print("2 - Segunda")
print("3 - Terça")
print("4 - Quarta")
print("5 - Quinta")
print("6 - Sexta")
print("7 - Sabado")
dia = int(input("Digite o numero referente ao dia: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
else:
    print("valor inválido")
    