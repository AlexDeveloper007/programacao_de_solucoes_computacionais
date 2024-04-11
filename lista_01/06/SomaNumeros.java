import java.util.Scanner;

public class SomaNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int somaPares = 0;
        int somaImpares = 0;
        int somaDivisiveisPor3 = 0;

        System.out.println("Digite dez números:");

        for (int i = 1; i <= 10; i++) {
            System.out.print("Número " + i + ": ");
            int numero = scanner.nextInt();

            // Verifica se o número é par e soma
            if (numero % 2 == 0) {
                somaPares += numero;
            }

            // Verifica se o número é ímpar e soma
            if (numero % 2 != 0) {
                somaImpares += numero;
            }

            // Verifica se o número é divisível por 3 e soma
            if (numero % 3 == 0) {
                somaDivisiveisPor3 += numero;
            }
        }

        // Exibindo os resultados
        System.out.println("Soma dos números pares: " + somaPares);
        System.out.println("Soma dos números ímpares: " + somaImpares);
        System.out.println("Soma dos números divisíveis por 3: " + somaDivisiveisPor3);

        scanner.close();
    }
}
