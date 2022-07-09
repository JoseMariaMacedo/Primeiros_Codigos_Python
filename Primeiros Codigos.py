from usuario import Usuario

usuario = Usuario("jose", 12, "macedo")

print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")



'''nome = "josé"
idade = 25
sobrenome = "macedo"

#print(nome, sobrenome, idade)

#print("Olá", nome, sobrenome, "sua idade é", idade)

print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")

#Aprendendo a utilizar o comando Input
idade2 = 1
while idade2 != 0:
    nome2 = input("Digite o seu nome: ")
    sobrenome2 = input("Digite seu sobrenome: ")
    idade2 = int(input("Digite sua idade: "))

    print(f"Olá {nome2} {sobrenome2}, sua idade é {idade2}")

#Operadores

#soma_idade = idade + idade2

#print(f"A soma da idades é {soma_idade}")

#subtracao_idade = idade - idade2
#print(f"A subtração das idades é {subtracao_idade}")

#multiplicacao_idade = idade * idade2
#print(f"A multiplicacao das idades é {multiplicacao_idade}")

#divisao_idade = idade / idade2
#print(f"A divisão das idades é {divisao_idade}")

#Estruturas de condição

    if idade2 <= 17:
        print(f"{nome2} é menor de idade")
    elif idade2 >= 18 and idade2 <= 50:
        print (f"{nome2} é adulto")
    else:
        print(f"{nome2} é idoso")

#Estruturas de repetição
'''
'''numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20. Ou maior para finalizar o laço" ))
    soma = soma + numero

print(soma)

for x in range(1, 10):
    y = x + 1
print(y) #10

#For-else e While-else

for x in range(1, 10):
    y = x + 1
else:
    print("loop encerrado com sucesso")
print(y) #10

numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    soma = soma + numero
else:
    print("loop encerrado com sucesso")
print(soma)

#Break
numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    if numero == 16:
       break
    soma = soma + numero
print(soma)

#Continue
numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    if numero == 16:
        continue
    soma = soma + numero

print(soma)
'''

#Importando métodos do arquivo usuário




