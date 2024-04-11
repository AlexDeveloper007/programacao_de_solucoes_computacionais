def main():
    total_pessoas = 25
    contador_idade_mais_50 = 0
    soma_altura_10a20 = 0
    contador_altura_10a20 = 0
    contador_peso_menos_40 = 0

    for i in range(1, total_pessoas + 1):
        print(f"Digite a idade da pessoa {i}:")
        idade = int(input())
        print("Digite a altura em metros (ex.: 1.75):")
        altura = float(input())
        print("Digite o peso em quilogramas:")
        peso = float(input())

        # Contando pessoas com idade superior a 50 anos
        if idade > 50:
            contador_idade_mais_50 += 1

        # Somando alturas das pessoas entre 10 e 20 anos
        if 10 <= idade <= 20:
            soma_altura_10a20 += altura
            contador_altura_10a20 += 1

        # Contando pessoas com peso inferior a 40 quilos
        if peso < 40:
            contador_peso_menos_40 += 1

    # Calculando a média das alturas das pessoas entre 10 e 20 anos
    if contador_altura_10a20 > 0:
        media_alturas = soma_altura_10a20 / contador_altura_10a20
    else:
        media_alturas = 0

    # Calculando a porcentagem de pessoas com peso inferior a 40 quilos
    porcentagem_peso_menos_40 = (contador_peso_menos_40 / total_pessoas) * 100

    # Exibindo os resultados
    print(f"Quantidade de pessoas com idade superior a 50 anos: {contador_idade_mais_50}")
    print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {media_alturas:.2f} m")
    print(f"Porcentagem de pessoas com peso inferior a 40 quilos: {porcentagem_peso_menos_40:.2f}%")

if __name__ == "__main__":
    main()
