def main():
    soma_pares = 0
    soma_impares = 0
    soma_divisiveis_por_3 = 0

    print("Digite dez números:")
    for i in range(1, 11):  # Repete 10 vezes
        numero = int(input(f"Digite o número {i}: "))

        # Verifica se o número é par
        if numero % 2 == 0:
            soma_pares += numero

        # Verifica se o número é ímpar
        if numero % 2 != 0:
            soma_impares += numero

        # Verifica se o número é divisível por 3
        if numero % 3 == 0:
            soma_divisiveis_por_3 += numero

    # Exibe os resultados
    print(f"Soma dos números pares: {soma_pares}")
    print(f"Soma dos números ímpares: {soma_impares}")
    print(f"Soma dos números divisíveis por 3: {soma_divisiveis_por_3}")

if __name__ == "__main__":
    main()
