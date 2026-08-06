# ==========================================
# Desafio 03 - Operações Matemáticas Simples
# ==========================================
# Descrição:
# Receba dois números e realize as quatro
# operações matemáticas básicas:
# - Soma
# - Subtração
# - Multiplicação
# - Divisão
# ==========================================

# Entrada de dados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Operações
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Evita divisão por zero
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Não é possível dividir por zero."

# Saída
print("\n===== Resultado =====")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
