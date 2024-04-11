import java.util.Scanner;

public class MaiorNumero {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        float maiorNumero = 0;
        int totalNumeros = 5;

        System.out.println("Insira " + totalNumeros + " números:");

        for (int i = 1; i <= totalNumeros; i++) {
            System.out.print("Número " + i + ": ");
            float numero = scanner.nextFloat();

            // Verifica se o número atual é maior que o maior número registrado
            if (numero > maiorNumero) {
                maiorNumero = numero;
            }
        }

        System.out.println("O maior número informado é: " + maiorNumero);
        scanner.close();
    }
}
