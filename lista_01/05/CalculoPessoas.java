import java.util.Scanner;

public class CalculoPessoas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalPessoas = 25;
        int contadorIdade50 = 0;
        int contadorFaixa10a20 = 0;
        double somaAlturas10a20 = 0;
        int contadorPesoMenor40 = 0;

        for (int i = 1; i <= totalPessoas; i++) {
            System.out.printf("Digite a idade da pessoa %d: ", i);
            int idade = scanner.nextInt();

            System.out.printf("Digite a altura da pessoa %d (em metros): ", i);
            double altura = scanner.nextDouble();

            System.out.printf("Digite o peso da pessoa %d (em kg): ", i);
            double peso = scanner.nextDouble();

            // a) Contagem de pessoas com mais de 50 anos
            if (idade > 50) {
                contadorIdade50++;
            }

            // b) Soma das alturas das pessoas entre 10 e 20 anos
            if (idade >= 10 && idade <= 20) {
                somaAlturas10a20 += altura;
                contadorFaixa10a20++;
            }

            // c) Contagem de pessoas com peso inferior a 40 kg
            if (peso < 40) {
                contadorPesoMenor40++;
            }
        }

        // Cálculo da média das alturas das pessoas entre 10 e 20 anos
        double mediaAlturas = 0;
        if (contadorFaixa10a20 > 0) {
            mediaAlturas = somaAlturas10a20 / contadorFaixa10a20;
        }

        // Cálculo da porcentagem de pessoas com peso menor que 40 kg
        double porcentagemPesoMenor40 = (double) contadorPesoMenor40 / totalPessoas * 100;

        // Exibição dos resultados
        System.out.println("Quantidade de pessoas com mais de 50 anos: " + contadorIdade50);
        System.out.printf("Média das alturas das pessoas com idade entre 10 e 20 anos: %.2f metros\n", mediaAlturas);
        System.out.printf("Porcentagem de pessoas com peso inferior a 40 kg: %.2f%%\n", porcentagemPesoMenor40);

        scanner.close();
    }
}
