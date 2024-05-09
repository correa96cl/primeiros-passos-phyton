print("Exemplo de importacao de um modulo padrao: ")
from math import sqrt

raiz_quadrada = sqrt()

print(f"A raiz quadrada de 25 e {raiz_quadrada}")


print("\nExemplo de criacao e utilizacao de um modulo personalizado")
import meu_modulo
from meu_modulo import saudacao, dobro
mensagem = saudacao("Gabriel")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")