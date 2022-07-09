from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sobrenome = input("Digite seu sobrenome: ")
    usuario = Usuario(nome, idade, sobrenome)
    lista_usuarios.append(usuario)
    
    if usuario.idade == 99:
        break
    if usuario.idade == 98:
        continue
    
    print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")
    
    if usuario.idade <= 17:
        print(f"{usuario.nome} é adolescente")
    elif usuario.idade >= 18 and usuario.idade <= 50:
        print(f"{usuario.nome} é adulto")
    else:
        print(f"{usuario.nome} é idoso")
        
    continuar = int(input("Deseja continuar cadastrado usuários? 0 = Sair 1 = Continuar "))

else:
    print("Lista de usuarios cadastrados: ")
    
    for i in lista_usuarios:
        print(f"Nome completo: {i.nome} {i.sobrenome} - Idade {i.idade}")
    
    print("O loop entrou no else")

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




