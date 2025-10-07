'''Exercício 1
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

while True:
    num = int(input("Escreva um numero de 0 a 10: "))
    if num >= 0 and num <= 10:
        print("Numero dentro do limite")
        break
    else:
        print("Numero errado!")
        continue
