nome_completo = "Marcelo Valderrama"
nome_completo_aspas = """Marcelo
Valderrama
"""

nome_completo_quebra = " marcelo \
    Valderrama"

nome = "Marcelo"
sobrenome = "valderrama"


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