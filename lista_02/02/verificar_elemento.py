def verificar_elemento(vetor, elemento):
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            posicoes.append(i)
    return posicoes

def main():
    vetor = []

    # Carregando o vetor
    for i in range(15):
        num = int(input(f"Digite o {i+1}º número: "))
        vetor.append(num)

    elemento = 30
    posicoes = verificar_elemento(vetor, elemento)

    if posicoes:
        print(f"O elemento {elemento} foi encontrado nas posições:")
        for posicao in posicoes:
            print(posicao)
    else:
        print(f"O elemento {elemento} não foi encontrado no vetor.")

if __name__ == "__main__":
    main()
