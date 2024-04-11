import java.util.Scanner;

public class CalculoPessoas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalPessoas = 25;
        int contadorIdadeMais50 = 0;
        double somaAltura10a20 = 0;
        int contadorAltura10a20 = 0;
        int contadorPesoMenos40 = 0;

        for (int i = 1; i <= totalPessoas; i++) {
            System.out.printf("Pessoa %d\n", i);
            System.out.print("Digite a idade: ");
            int idade = scanner.nextInt();
            System.out.print("Digite a altura em metros (ex.: 1,75): ");
            double altura = scanner.nextDouble();
            System.out.print("Digite o peso em quilogramas: ");
            double peso = scanner.nextDouble();

            // Contando pessoas com idade superior a 50 anos
            if (idade > 50) {
                contadorIdadeMais50++;
            }

            // Somando alturas das pessoas entre 10 e 20 anos
            if (idade >= 10 && idade <= 20) {
                somaAltura10a20 += altura;
                contadorAltura10a20++;
            }

            // Contando pessoas com peso inferior a 40 quilos
            if (peso < 40) {
                contadorPesoMenos40++;
            }
        }

        // Calculando a média das alturas das pessoas entre 10 e 20 anos
        double mediaAlturas = (contadorAltura10a20 > 0) ? somaAltura10a20 / contadorAltura10a20 : 0;

        // Calculando a porcentagem de pessoas com peso inferior a 40 kg
        double porcentagemPesoMenos40 = ((double) contadorPesoMenos40 / totalPessoas) * 100;

        // Exibindo os resultados
        System.out.println("Quantidade de pessoas com idade superior a 50 anos: " + contadorIdadeMais50);
        System.out.printf("Média das alturas das pessoas com idade entre 10 e 20 anos: %.2f m\n", mediaAlturas);
        System.out.printf("Porcentagem de pessoas com peso inferior a 40 quilos: %.2f%%\n", porcentagemPesoMenos40);

        scanner.close();
    }
}
