def eh_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    tamanho_vetor = 15

    # Leitura do vetor de números inteiros
    vetor = []
    for i in range(tamanho_vetor):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor.append(num)

    # Criando o vetor resultante com apenas números primos
    vetor_primos = [num for num in vetor if eh_primo(num)]

    # Escrevendo o vetor resultante
    print("\nVetor resultante contendo apenas números primos:")
    for primo in vetor_primos:
        print(primo)

if __name__ == "__main__":
    main()
