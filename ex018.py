'''Exercício 18
Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

data = input('Coloque uma data no formato dd/mm/aaaa: ')
sepa = data.split('/')
# não é uma validação muito boa mas estamos na simplicidade por enquanto
if int(sepa[0]) <= 31 and int(sepa[1]) <= 12 and int(sepa[2]) <= 9999:
    print("Data valida")
else:
    print("Data invalida")