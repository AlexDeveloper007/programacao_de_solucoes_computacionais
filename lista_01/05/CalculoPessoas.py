def main():
    total_pessoas = 25
    pessoas_mais_50_anos = 0
    soma_alturas_10_20 = 0
    contador_10_20 = 0
    contador_peso_menor_40 = 0

    for i in range(1, total_pessoas + 1):
        print(f"Digite as informações para a pessoa {i}:")
        idade = int(input("Idade: "))
        altura = float(input("Altura (em metros): "))
        peso = float(input("Peso (em quilogramas): "))

        # a) Quantidade de pessoas com idade superior a 50 anos
        if idade > 50:
            pessoas_mais_50_anos += 1

        # b) A média das alturas das pessoas com idade entre 10 e 20 anos
        if 10 <= idade <= 20:
            soma_alturas_10_20 += altura
            contador_10_20 += 1

        # c) A porcentagem de pessoas com peso inferior a 40 quilos
        if peso < 40:
            contador_peso_menor_40 += 1

    # Calcular média de alturas
    if contador_10_20 > 0:
        media_alturas_10_20 = soma_alturas_10_20 / contador_10_20
    else:
        media_alturas_10_20 = 0

    # Calcular porcentagem
    porcentagem_peso_menor_40 = (contador_peso_menor_40 / total_pessoas) * 100

    # Resultados
    print(f"\nQuantidade de pessoas com mais de 50 anos: {pessoas_mais_50_anos}")
    print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {media_alturas_10_20:.2f} metros")
    print(f"Porcentagem de pessoas com peso inferior a 40 kg: {porcentagem_peso_menor_40:.2f}%")

if __name__ == "__main__":
    main()
