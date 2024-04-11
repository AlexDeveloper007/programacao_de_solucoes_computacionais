import java.util.Scanner;

public class CalculoPeso {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalPessoas = 7;
        int somaIdades = 0;
        int idade, pessoasMais90 = 0;
        double peso;

        for (int i = 1; i <= totalPessoas; i++) {
            System.out.printf("Digite a idade da pessoa %d: ", i);
            idade = scanner.nextInt();
            System.out.printf("Digite o peso da pessoa %d (em kg): ", i);
            peso = scanner.nextDouble();

            // Soma das idades para cálculo da média
            somaIdades += idade;

            // Contador de pessoas com mais de 90 quilos
            if (peso > 90) {
                pessoasMais90++;
            }
        }

        // Calcula a média das idades
        double mediaIdades = somaIdades / (double) totalPessoas;

        // Exibe os resultados
        System.out.println("Quantidade de pessoas com mais de 90 kg: " + pessoasMais90);
        System.out.printf("Média das idades das sete pessoas: %.2f anos\n", mediaIdades);

        scanner.close();
    }
}
