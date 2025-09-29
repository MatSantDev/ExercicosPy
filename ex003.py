'''Exercício 03
Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

F - Feminino
M - Masculino
Sexo Inválido.'''

letra = input("Homem[M] ou Mulher[F]")
if(letra == 'M'):
    print("Senhor")
elif(letra == 'F'):
    print("Senhora")
else:
    print("Sexo Inválido")