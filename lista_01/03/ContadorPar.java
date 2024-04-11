import java.util.Scanner;

public class ContadorPar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalNumeros = 10;
        int contaPares = 0;

        System.out.println("Digite 10 números inteiros:");

        for (int i = 1; i <= totalNumeros; i++) {
            System.out.print("Número " + i + ": ");
            int numero = scanner.nextInt();

            // Verifica se o número é par
            if (numero % 2 == 0) {
                contaPares++;
            }
        }

        System.out.println("Você digitou " + contaPares + " números pares.");
        scanner.close();
    }
}
