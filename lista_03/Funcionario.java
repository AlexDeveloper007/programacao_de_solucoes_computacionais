public class Funcionario implements Trabalhador {
    protected double salario;
    protected String departamento;

    public Funcionario(double salario, String departamento) {
        this.salario = salario;
        this.departamento = departamento;
    }

    public void exibirInformacoes() {
        System.out.println("Salário: " + salario);
        System.out.println("Departamento: " + departamento);
    }

    public static void main(String[] args) {
        Funcionario funcionario = new Funcionario(7500.0, "Desenvolvimento");
        funcionario.exibirInformacoes();
        funcionario.trabalhar();
    }

    // Implementando o método trabalhar da interface Trabalhador
    @Override
    public void trabalhar() {
        System.out.println("O funcionário está trabalhando.");
    }
}
