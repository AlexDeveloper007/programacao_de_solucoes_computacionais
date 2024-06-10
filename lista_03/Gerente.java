public class Gerente extends Funcionario { // << Não implementei a interface Trabalhador aqui pois a Funcionario
                                           // extendida já implementa
    private double bonus;

    public Gerente(double salario, String departamento, double bonus) {
        super(salario, departamento);
        this.bonus = bonus;
    }

    @Override
    public void exibirInformacoes() {
        super.exibirInformacoes();
        System.out.println("Bônus: " + bonus);
    }

    public static void main(String[] args) {
        Gerente gerente = new Gerente(8000.0, "Diretoria", 3000.0);
        gerente.exibirInformacoes();
        gerente.trabalhar();
    }

    @Override
    public void trabalhar() {
        System.out.println("O gerente está trabalhando.");
    }
}
