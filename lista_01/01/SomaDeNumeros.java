import java.util.Scanner;

public class SomaDeNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int soma = 0;
        int totalNumeros = 10;

        System.out.println("Digite " + totalNumeros + " números inteiros:");

        for (int i = 1; i <= totalNumeros; i++) {
            System.out.print("Número " + i + ": ");
            int numero = scanner.nextInt();
            soma += numero;
        }

        System.out.println("A soma dos números é: " + soma);
        scanner.close();
    }
}
