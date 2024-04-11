def main():
    total_pessoas = 7
    soma_idades = 0
    pessoas_mais_90kg = 0

    for i in range(1, total_pessoas + 1):
        print(f"Digite a idade da pessoa {i}:")
        idade = int(input())
        print(f"Digite o peso da pessoa {i} (em kg):")
        peso = float(input())

        soma_idades += idade  # Soma de todas as idades

        if peso > 90:  # Contagem de pessoas com mais de 90kg
            pessoas_mais_90kg += 1

    media_idades = soma_idades / total_pessoas  # Cálculo da média das idades

    # Exibindo os resultados
    print(f"Quantidade de pessoas com mais de 90 quilos: {pessoas_mais_90kg}")
    print(f"Média das idades das sete pessoas: {media_idades:.2f}")

if __name__ == "__main__":
    main()
