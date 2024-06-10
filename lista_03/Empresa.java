public class Empresa {
    public void adicionarTrabalhador(Trabalhador trabalhador) {
        trabalhador.trabalhar();
    }

    public static void main(String[] args) {
        Empresa empresa = new Empresa();

        Funcionario funcionario = new Funcionario(7000.0, "Desenvolvimento");
        Gerente gerente = new Gerente(8500.0, "Marketing", 2200.0);

        empresa.adicionarTrabalhador(funcionario);
        empresa.adicionarTrabalhador(gerente);
    }
}
