'''Exercício 27
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''


mora = float(input("Peso dos Morangos: "))
maca = float(input("Peso das Maças: "))
valorMo = 0
valorMa = 0
frutas = mora + maca

if mora <= 5:
    valorMo = 2.5
else:
    valorMo = 2.2

if maca <= 5:
    valorMa = 1.8
else:
    valorMa = 1.5

total = mora * valorMo + maca * valorMa

if frutas > 8 or total > 25:
    desc = 10
else:
    desc = 0

total = total - (total * desc / 100)
print(f"Valor a ser pago: {total}")