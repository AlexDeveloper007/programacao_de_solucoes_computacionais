def solicitar_numeros_e_somar():
    soma = 0
    total_numeros = 10
    print(f"Por favor, insira {total_numeros} números inteiros.")

    for i in range(1, total_numeros + 1):
        while True:
            try:
                numero = int(input(f"Digite o número {i}: "))
                break
            except ValueError:
                print("Por favor, insira um valor inteiro válido.")
        
        soma += numero

    print("A soma dos números é:", soma)

if __name__ == "__main__":
    solicitar_numeros_e_somar()
