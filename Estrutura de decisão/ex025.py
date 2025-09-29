'''Exercício 25
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

print("Responda as perguntas com 1 para verdadeiro e 0 para falso")
per1 = int(input("Telefonou para a vítima? R:"))
per2 = int(input("Esteve no local do crime? R:"))
per3 = int(input("Mora perto da vítima? R:"))
per4 = int(input("Devia para a vítima R:"))
per5 = int(input("Já trabalhou com a vítima? R:"))
soma = per1 + per2 + per3 + per4 + per5

if soma == 2:
    print("Suspeita")
elif soma >= 3 and soma <=4:
    print("Cúmplice")
elif soma == 5:
    print("Assassino")
else:
    print("Inocente")