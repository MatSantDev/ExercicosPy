'''Exercício 08
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valorhora = float(input("Quanto voce ganha por hora:  "))
horastrabalhadas = float(input("Quantas horas trabalhou: "))
salario = valorhora * horastrabalhadas
print(f'Voce recebe esse mês R${salario}')
