def obter_ultimo_nome(nome_completo):
    partes_nome = nome_completo.split()
    return partes_nome[-1]

def main():
    nome_completo = input("Digite o nome completo da pessoa: ")
    ultimo_nome = obter_ultimo_nome(nome_completo)
    print(f"O último nome da pessoa é: {ultimo_nome}")

if __name__ == "__main__":
    main()
