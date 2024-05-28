def main():
    vetor = []

    # Carregando o vetor
    for i in range(6):
        num = int(input(f"Digite o {i+1}º número: "))
        vetor.append(num)

    # Calculando e mostrando a quantidade e os números pares
    pares = [num for num in vetor if num % 2 == 0]
    print(f"Quantidade de números pares: {len(pares)}")
    if len(pares) > 0:
        print("Números pares:", ', '.join(map(str, pares)))
    else:
        print("Não há números pares.")

    # Calculando e mostrando a quantidade e os números ímpares
    impares = [num for num in vetor if num % 2 != 0]
    print(f"Quantidade de números ímpares: {len(impares)}")
    if len(impares) > 0:
        print("Números ímpares:", ', '.join(map(str, impares)))
    else:
        print("Não há números ímpares.")

if __name__ == "__main__":
    main()
