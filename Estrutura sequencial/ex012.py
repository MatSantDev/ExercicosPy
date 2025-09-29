'''Exercício 12
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula: Gigabytes * 1024'''

gigabytes = int(input("Quantos Gigabytes tem: "))
megabytes = gigabytes * 1024
print(f"Seu arquivo que tem {gigabytes} gigabytes tem em megabytes {megabytes}")
