'''Exercício 15
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valorHora = float(input("quanto você ganha por hora: "))
horasTrabalhadas = int(input("número de horas trabalhadas no mês: "))
salarioBruto = valorHora * horasTrabalhadas
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = impostoRenda + inss + sindicato
salarioLiquido = salarioBruto - descontos
print(f"Seu salario bruto é R${salarioBruto}")
print(f"O imposto de renda é R${impostoRenda}")
print(f"O inss é R${inss}")
print(f"O sindicato é R${sindicato}")
print(f"O Seu salrio liquido é R${salarioLiquido}")
