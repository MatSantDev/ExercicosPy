'''Exercício 28
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

tipo = input("Tipo de Carne: ")
peso = float(input("Peso: "))

if peso <= 5:
    if tipo == 'File Duplo':
        Valor = 4.9
    elif tipo == 'Alcatra':
        valor = 5.9
    elif tipo == 'Picanha':
        valor = 6.9
    else:
        print("Tipo errado")
        exit()
else:
    if tipo == 'File Duplo':
        Valor = 5.8
    elif tipo == 'Alcatra':
        valor = 6.8
    elif tipo == 'Picanha':
        valor = 7.8
    else:
        print("Tipo errado")
        exit()

cartao = input("Qual metodo de compra irá utilizar: ")

if cartao == 'Tabajara':
    desc = 5
else:
    desc = 0

print(f"Tipo de carne: {tipo}")
print(f"Peso da carne: {peso}")
print(f"Preço total: {(valor * peso):.2f}")
print(f"Tipo de pagamento: {cartao}")
print(f"Valor do desconto: {(valor * peso * desc / 100):.2f}")
print(f"Valor a pagar: {((valor * peso) - (valor * peso * desc / 100)):.2f}")
