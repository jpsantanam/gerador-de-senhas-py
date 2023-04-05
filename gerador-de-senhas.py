import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao Gerador de Senhas!")
numeroLetras = int(input("Quantas letras você gostaria na sua senha?\n"))
numeroSimbolos = int(input(f"Quantos símbolos você gostaria?\n"))
numeroNumeros = int(input(f"Quantos números você gostaria?\n"))

tamanhoSenha = numeroLetras + numeroSimbolos + numeroNumeros
senhaVetor = []

for letra in range(0, numeroLetras):
    senhaVetor.append(random.choice(letras))
for simbolo in range(0, numeroSimbolos):
    senhaVetor.append(random.choice(numeros))
for numero in range(0, numeroNumeros):
    senhaVetor.append(random.choice(simbolos))

random.shuffle(senhaVetor)
senhaFinal = "".join(senhaVetor)

print(senhaFinal)

