'''Exercício 10
Faça um programa que pergunte em que turno você estuda. Peça para digitar:

M - Matutino
V - Vespertino
N - Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input("Que horas voce estuda - [M]atutino, [V]espertino ou [N]oturno: ")
if turno == 'M' or turno == 'Matutino':
    print("Bom Dia!")
elif turno == 'V' or turno == 'Vespertino':
    print("Boa Tarde!")
elif turno == 'N' or turno == 'Noturno':
    print("Boa noite!")
else:
    print("Valor Inválido!")