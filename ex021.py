'''Exercício 21
Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

saque = int(input("Qual o valor do saque: "))
if(saque >= 10) and (saque <= 600):
    cen = saque // 100
    cin = (saque - cen*100) // 50
    dez = (saque - cen*100 - cin*50) // 10
    cinco = (saque - cen*100 - cin*50 - dez*10) // 5
    uni = (saque - cen*100 - cin*50 - dez*10 - cinco*5) // 1
    print(f"Para sacar a quantia de {saque} reais, o programa fornece {cen} notas de 100, {cin} nota de 50, {dez} nota de 10, {cinco} nota de 5 e {uni} nota de 1")
else:
    print("Não pode sacar")