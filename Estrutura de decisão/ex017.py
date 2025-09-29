'''Exercício 17
Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

ano = int(input("Ano: "))

if(ano % 4 == 0) and (ano % 100 != 0):
    print("Este ano é Bissexto")
elif(ano % 400 == 0):
    print("Este ano é Bissexto")
else:
    print("Este ano não é Bissexto")