def calcular_comissao(vendas, comissoes):
    comissoes_totais = []
    for venda, comissao in zip(vendas, comissoes):
        comissao_total = venda * (comissao / 100)
        comissoes_totais.append(comissao_total)
    return comissoes_totais

def main():
    total_vendedores = 10

    vendas = []
    comissoes = []
    nomes = []

    # Obtendo os dados dos vendedores
    for i in range(total_vendedores):
        nome = input(f"Digite o nome do vendedor {i+1}: ")
        nomes.append(nome)
        venda = float(input(f"Digite o total das vendas de {nome}: "))
        vendas.append(venda)
        comissao = float(input(f"Digite o percentual de comissão de {nome} (%): "))
        comissoes.append(comissao)

    # Calculando as comissões totais dos vendedores
    comissoes_totais = calcular_comissao(vendas, comissoes)

    # Mostrando o relatório
    print("\nRelatório de Comissões:")
    maior_comissao = 0
    menor_comissao = float('inf')
    for nome, comissao_total in zip(nomes, comissoes_totais):
        print(f"{nome}: R${comissao_total:.2f}")
        if comissao_total > maior_comissao:
            maior_comissao = comissao_total
            vendedor_maior_comissao = nome
        if comissao_total < menor_comissao:
            menor_comissao = comissao_total
            vendedor_menor_comissao = nome

    total_vendas = sum(vendas)

    print(f"\nTotal das vendas de todos os vendedores: R${total_vendas:.2f}")
    print(f"Maior comissão: {vendedor_maior_comissao} - R${maior_comissao:.2f}")
    print(f"Menor comissão: {vendedor_menor_comissao} - R${menor_comissao:.2f}")

if __name__ == "__main__":
    main()
