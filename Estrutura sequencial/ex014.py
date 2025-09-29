'''Exercício 14
João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

peso_max = 50
peso = float(input("Qual o peso do peixe: "))
excesso = peso - peso_max
multa = int(excesso) * 4
print(f"O peixe tem o peso de {peso} tendo um excesso de {excesso:.2f}, a multa a pagar é de R${multa}")
