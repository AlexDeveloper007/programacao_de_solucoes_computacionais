def main():
    print("Números entre 1000 e 2000 que ao serem divisíveis por 5 produzem resto 3:")
    for i in range(1000, 2001):
        if i % 5 == 3:
            print(i)

if __name__ == "__main__":
    main()
