'''Exercício 18
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

mb = float(input("tamanho de um arquivo para download (em MB): "))
mbps = float(input("velocidade de um link de Internet (em Mbps): "))
tempoS = mb / mbps
tempoM = tempoS / 60
print(f"O tempo de download em minuto é {tempoM:.2f}")