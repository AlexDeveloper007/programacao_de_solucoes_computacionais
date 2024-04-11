import java.util.Scanner;

public class DadosPessoas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalPessoas = 7;
        int somaIdades = 0;
        int contadorPesoMaior90 = 0;

        for (int i = 1; i <= totalPessoas; i++) {
            System.out.print("Digite a idade da pessoa " + i + ": ");
            int idade = scanner.nextInt();
            System.out.print("Digite o peso da pessoa " + i + " (em kg): ");
            double peso = scanner.nextDouble();

            // Soma de todas as idades
            somaIdades += idade;

            // Contador de pessoas com mais de 90kg
            if (peso > 90) {
                contadorPesoMaior90++;
            }
        }

        // Calculando a média das idades
        double mediaIdades = somaIdades / (double) totalPessoas;

        // Exibindo os resultados
        System.out.println("Quantidade de pessoas com mais de 90 quilos: " + contadorPesoMaior90);
        System.out.println("Média das idades das sete pessoas: " + mediaIdades);

        scanner.close();
    }
}
