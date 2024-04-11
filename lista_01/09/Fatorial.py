def fatorial_iterativo(n):
    if n == 0:
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

# Solicitando entrada do usuário
n = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial_iterativo(n)
print(f"O fatorial de {n} é {resultado}")
