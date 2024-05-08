print("For utilizando lista")
lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Marcelo", "idade": 42, "cidade": "Rio de Janeiro"}
print("For utilizando diccionario - chaves")
for chave in pessoa.keys():
    print(chave)
print("\nFor utilizando diccionario - valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando diccionario - items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print(list(range(0,10)))

print("\n Utilizando a funcao range()")
for numero in range(6):
    print("Numero : ", numero)

print("\n Utilizando a funcao range() com len()")

lista = [1,2,3,4,5]
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)


lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice} : {valor}")
    if indice == 1:
        print("Indice 1")