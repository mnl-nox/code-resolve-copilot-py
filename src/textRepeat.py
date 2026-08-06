# ==========================================
# Desafio 02 - Repetição de Texto
# ==========================================
# Descrição:
# Receba uma string e um número inteiro.
# Em seguida, exiba a string repetida
# a quantidade de vezes informada.
# ==========================================

# Entrada de dados
texto = input("Digite um texto: ")
quantidade = int(input("Digite a quantidade de repetições: "))

# Saída
print("\n===== Resultado =====")
for _ in range(quantidade):
    print(texto)

# Outro metodo em Python.


# texto = input("Digite um texto: ")
# quantidade = int(input("Digite a quantidade de repetições: "))
# print((texto + "\n") * quantidade)
