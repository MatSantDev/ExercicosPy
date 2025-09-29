'''Exercício 20
Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

nota1 = float(input("1º Nota: "))
nota2 = float(input("2º Nota: "))
nota3 = float(input("3º Nota: "))

media = (nota1 + nota2 + nota3)/3

if(media < 7):
    men = "Reprovado"
elif (media == 10):
    men = "Aprovado com Distinção"
else:
    men = "Aprovado"

print(f"A media foi {media:.2f} e vc foi {men}")