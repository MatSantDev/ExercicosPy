'''Exercício 24
Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

num1 = float(input("Escreva um numero: "))
num2 = float(input("Escreva outro numero: "))
opera = input("Qual operação deseja? (+, -, /, *): ")

if(opera == '+'):
    res = num1 + num2
elif opera == '-':
    res = num1 - num2
elif opera == '/':
    res = num1 / num2
elif opera == '*':
    res = num1 * num2
else:
    print("Operação invalida")


print(f"O resultado é {res}")
if(res % 2 == 0):
    print("É par")
else:
    print("É impar")

if(res >= 0):
    print("É positivo")
else:
    print("É negativo")

if res.is_integer():
    print("O número é inteiro")
else:
    print("O número é decimal")
