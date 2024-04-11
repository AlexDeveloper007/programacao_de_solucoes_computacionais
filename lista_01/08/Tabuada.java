import java.util.Scanner;

public class Tabuada {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número para ver sua tabuada de 0 a 100: ");
        int numero = scanner.nextInt();

        System.out.println("Tabuada de " + numero + " de 0 a 100:");
        for (int i = 0; i <= 100; i++) {
            System.out.println(numero + " x " + i + " = " + (numero * i));
        }

        scanner.close();
    }
}
