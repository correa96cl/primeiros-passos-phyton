pessoa =  {"nome": "Joao", "idade": 30, "cidade": "Sao Paulo"}

print("Meu diccionario de exemplo : ", pessoa)


print("Nome : ", pessoa["nome"])
print("Idade : ", pessoa["idade"])
print("Cidade : ", pessoa["cidade"])
pessoa["sobrenome"] = "Silva"
print("Sobrenome : ", pessoa['sobrenome'])

del pessoa["sobrenome"]

chaves = pessoa.keys()
print("Chaves : ", chaves)

chavesLista = list(pessoa.keys())

print("Primeira chave : ", chavesLista[0])

valores = list(pessoa.values())
print("Valores do diccionarioos : ", valores)


itens = list(pessoa.items())

print("Items : ", itens)

print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))