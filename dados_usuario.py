"""
Métodos para receber dados do usuário
Todos os dados recebidos através de um INPUT é do tipo STRING
"""


# Método 1
nome = input("Digite o seu nome: ")
print("Bem-vindo %s" % nome)
idade = input("Digite a sua idade: ")
print("%s tem %s anos" % (nome, idade))


# Método 2
nome = input("Digite o seu nome: ")
print("Bem-vindo {}" .format(nome))
idade = input("Digite a sua idade: ")
print("{} tem {} anos" .format(nome, idade))


# Método 3 - Mais atual
nome = input("Digite o seu nome: ")
print(f"Bem-vindo {nome}")
idade = input("Digite a sua idade: ")
print(f"{nome} tem {idade} anos")


# Cast - conversão de um tipo de dado para outro
print(f"{nome} nasceu em {2022 - int(idade)}")
