import math

def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * raio ** 3
    return volume

def main():
    raio = float(input("Digite o raio da esfera: "))

    if raio < 0:
        print("O raio da esfera deve ser um número positivo.")
    else:
        volume = calcular_volume_esfera(raio)
        print(f"O volume da esfera de raio {raio} é: {volume:.2f}")

if __name__ == "__main__":
    main()
