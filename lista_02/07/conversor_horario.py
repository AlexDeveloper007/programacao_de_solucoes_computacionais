def converter_para_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

def main():
    horas = int(input("Digite o número de horas: "))
    minutos = int(input("Digite o número de minutos: "))
    segundos = int(input("Digite o número de segundos: "))

    total_segundos = converter_para_segundos(horas, minutos, segundos)
    print(f"{horas}h, {minutos}min e {segundos}seg correspondem a {total_segundos} segundos.")

if __name__ == "__main__":
    main()
