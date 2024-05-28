def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    while numero < 0:
        print("O número precisa ser inteiro positivo.")
        numero = int(input("Digite um número inteiro positivo: "))

    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")

if __name__ == "__main__":
    main()
