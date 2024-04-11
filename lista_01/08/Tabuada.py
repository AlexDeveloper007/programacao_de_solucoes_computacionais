def main():
    numero = int(input("Digite um número para ver sua tabuada de 0 a 100: "))
    print(f"Tabuada de {numero} de 0 a 100:")
    
    for i in range(101):  # Loop de 0 a 100
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    main()
