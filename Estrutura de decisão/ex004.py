'''Exercício 04
Faça um programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input("Escreva uma letra: ")
vogais = ['a', 'e', 'i' ,'o', 'u']
if(letra in vogais):
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante")
