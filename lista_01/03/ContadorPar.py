def contar_numeros_pares():
    total_numeros = 10
    conta_pares = 0  
    print("Informe 10 números inteiros:")

    for i in range(1, total_numeros + 1):
        try:
            numero = int(input(f"Número {i}: "))
            # Verifica se o número é par
            if numero % 2 == 0:
                conta_pares += 1
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")
            i -= 1  # Decrementa o índice para repetir a entrada do número

    print(f"Você digitou {conta_pares} números pares.")

if __name__ == "__main__":
    contar_numeros_pares()
