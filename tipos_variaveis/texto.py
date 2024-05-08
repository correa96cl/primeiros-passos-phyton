nome_completo = "Marcelo Valderrama"
nome_completo_aspas = """Marcelo
Valderrama
"""

nome_completo_quebra = " marcelo \
    Valderrama"

nome = "Marcelo"
sobrenome = "valderrama"
telefone = '(21)980038543'


#formatacao

print("Nome completo", nome_completo)
print("Nome completo 2a forma : "+ nome_completo)
print("Nome completo 3a forma : "+ "Marcelo" + " Valderrama")
print("Nome completo 4a forma : " + "Marcelo" , "Valderrama")
print("Nome completo 5a forma : ", nome_completo_aspas)
print("Nome completo 6a forma : ", nome_completo_quebra)
print("Nome copmpleto 7a forma : %s" % nome_completo)
print("Nome completo 8a forma : %s %s" % (nome, sobrenome))
print(f"Nome completo 9a forma : {nome} {sobrenome}")
print("Nome completo 10 a forma : {} {}".format(nome, sobrenome))
print("Nome upper case", nome.upper())
print("Nome com lowercase", nome.lower())
print("Primeiro carater do string", nome[0])
print("Contar algumas letras do carater :", nome_completo.count("m"))
print("Encontrar algum carater : ", nome_completo.find("a"))
print("Encode : ", nome_completo.encode())
print("Encode depois decode", nome_completo.encode().decode())
print("Replace", nome_completo.replace("a", "b"))
print("Numerico replace", telefone.replace("(", "").replace(")", ""))
print("Adicionar separador : ", "-".join(nome_completo))
print("Split de um string : ", nome_completo.split())
print("Split de um carater outra forma : ", nome_completo.split(" "))
print("Eliminar careteres de um string", nome_completo.strip("a"))
print("Eliminar carateres de um string : ", nome_completo.rstrip("a"))
print("Start : ", nome_completo.startswith("Ma"))
print("Contains : ", "Ma" in nome_completo)
print("Nao ecnontrado : ", "Ma" not in nome_completo)