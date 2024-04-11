def encontrar_maior_numero():
    maior_numero = 0
    total_numeros = 5

    print(f"Insira {total_numeros} números:")

    for i in range(1, total_numeros + 1):
        while True:
            try:
                numero = float(input(f"Digite o número {i}: "))
                break
            except ValueError:
                print("Insira um valor válido de ponto flutuante.")

        if numero > maior_numero:
            maior_numero = numero

    print("O maior número é:", maior_numero)

if __name__ == "__main__":
    encontrar_maior_numero()
