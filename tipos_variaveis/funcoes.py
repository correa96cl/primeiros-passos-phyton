def saudacao(nome):
    print(f"Ola, {nome}!")

print("\n Chamando a funcao saudacao")
saudacao("Alice")
saudacao("Bob")

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando funcao quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado:", resultado_quadrado)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a funcao soma : ")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e o numero %s é %s" % (numero1, numero2, resultado_soma))