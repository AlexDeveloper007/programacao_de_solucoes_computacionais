import math

def calcular_s(N):
    S = 0
    for i in range(1, N + 1):
        S += 1 / math.factorial(i)
    return S

def main():
    N = int(input("Digite um valor inteiro positivo para N: "))
    while N <= 0:
        print("N deve ser um valor inteiro positivo.")
        N = int(input("Digite um valor inteiro positivo para N: "))

    resultado = calcular_s(N)
    print(f"O valor de S é: {resultado:.6f}")

if __name__ == "__main__":
    main()
