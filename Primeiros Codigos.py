nome = "josé"
idade = 25
sobrenome = "macedo"

#print(nome, sobrenome, idade)

#print("Olá", nome, sobrenome, "sua idade é", idade)

print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

#Aprendendo a utilizar o comando Input

nome2 = input("Digite o seu nome: ")
sobrenome2 = input("Digite seu sobrenome: ")
idade2 = int(input("Digite sua idade: "))

print(f"Olá {nome2} {sobrenome2}, sua idade é {idade2}")

#Operadores

soma_idade = idade + idade2

print(f"A soma da idades é {soma_idade}")

subtracao_idade = idade - idade2
print(f"A subtração das idades é {subtracao_idade}")

multiplicacao_idade = idade * idade2
print(f"A multiplicacao das idades é {multiplicacao_idade}")

divisao_idade = idade / idade2
print(f"A divisão das idades é {divisao_idade}")

#Estruturas de condição

if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")

if idade2 <= 17:
    print(f"{nome2} é menor de idade")
elif idade2 >= 18 and idade2 <= 50:
    print (f"{nome2} é adulto")
else:
    print(f"{nome2} é idoso")

