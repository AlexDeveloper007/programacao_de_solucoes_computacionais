def main():
    total_produtos = 5

    nomes = []
    precos = []

    # Pegando os dados dos produtos
    for i in range(total_produtos):
        nome = input(f"Digite o nome do produto {i+1}: ")
        nomes.append(nome)
        preco = float(input(f"Digite o preço do produto {nome}: R$"))
        precos.append(preco)

    # Calculando e mostrando a quantidade de produtos com preço menor que R$ 50,00
    produtos_inferior_50 = sum(1 for preco in precos if preco < 50)
    print(f"\nQuantidade de produtos com preço inferior a R$ 50,00: {produtos_inferior_50}")

    # Mostrando os nomes dos produtos com preço entre R$ 50,00 e R$ 100,00
    print("\nProdutos com preço entre R$ 50,00 e R$ 100,00:")
    for nome, preco in zip(nomes, precos):
        if 50 <= preco <= 100:
            print(nome)

    # Calculando a média dos preços dos produtos com preço superior a R$ 100,00
    produtos_superior_100 = [preco for preco in precos if preco > 100]
    if produtos_superior_100:
        media_precos_superior_100 = sum(produtos_superior_100) / len(produtos_superior_100)
        print(f"\nMédia dos preços dos produtos com preço superior a R$ 100,00: R${media_precos_superior_100:.2f}")
    else:
        print("\nNão há produtos com preço superior a R$ 100,00.")

if __name__ == "__main__":
    main()
