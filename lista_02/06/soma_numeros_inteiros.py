def soma_n_inteiros(N):
    soma = 0
    for i in range(1, N + 1):
        soma += i
    return soma

def main():
    numero = int(input("Digite um número inteiro e positivo: "))
    while numero <= 0:
        print("O número precisa ser inteiro e positivo.")
        numero = int(input("Digite um número inteiro e positivo: "))

    resultado = soma_n_inteiros(numero)
    print(f"A soma dos N números inteiros entre 1 e {numero} é: {resultado}")

if __name__ == "__main__":
    main()
