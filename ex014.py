'''Exercício 14
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
Entre 9.0 e 10.0         A
Entre 7.5 e 9.0          B
Entre 6.0 e 7.5          C
Entre 4.0 e 6.0          D
Entre 4.0 e zero         E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

nota1 = float(input("Valor da 1º nota: "))
nota2 = float(input("Valor da 2º nota: "))
media = (nota1 + nota2) / 2

if media >= 9.0:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

print(f"1º Nota: {nota1} | 2º Nota: {nota2} | Média: {media} | Conceito: {conceito}")
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print(f"APROVADO")
else:
    print(f"REPROVADO")