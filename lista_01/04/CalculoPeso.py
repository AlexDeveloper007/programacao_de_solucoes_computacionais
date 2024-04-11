def coletar_dados_pessoais():
    total_pessoas = 7
    soma_idades = 0
    pessoas_mais_90kg = 0

    for i in range(1, total_pessoas + 1):
        print(f"Digite as informações para a pessoa {i}:")
        try:
            idade = int(input("Idade: "))
            peso = float(input("Peso (em kg): "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue  # Pula para a próxima iteração do loop

        soma_idades += idade

        if peso > 90:
            pessoas_mais_90kg += 1

    media_idades = soma_idades / total_pessoas

    print(f"Quantidade de pessoas com mais de 90 kg: {pessoas_mais_90kg}")
    print(f"Média das idades das sete pessoas: {media_idades:.2f} anos")

if __name__ == "__main__":
    coletar_dados_pessoais()
