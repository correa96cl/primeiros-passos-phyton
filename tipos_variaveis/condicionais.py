idade = int(input("Quantos anos voces tem? "))
if idade >= 18:
    print("Voce e maior de idade.")
elif idade >= 12:
    print("Voce e um adosclenete")
else:
    print("Voce e menor de idade.")

mensagem = "Pode tirar a carteira" if idade >= 18 else "Voce nao pode tirar a carteira de habilitacao"
print(mensagem)


