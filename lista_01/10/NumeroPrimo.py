def is_prime(num):
    """ Retorna True se o número é primo, caso contrário False. """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    try:
        number = int(input("Digite um número para verificar se é primo: "))
        if is_prime(number):
            print(f"{number} é um número primo.")
        else:
            print(f"{number} não é um número primo.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
