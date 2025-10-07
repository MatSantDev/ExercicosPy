'''Exercício 3
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Estado Civil: 's', 'c', 'v', 'd';'''

while True:
    nome = input("Escreva seu nome: ")
    idade = int(input("Sua idade: "))
    salario = float(input("Seu salario: "))
    estadoCivil = input("Estado Civil: ('s', 'c', 'v', 'd'): ")

    