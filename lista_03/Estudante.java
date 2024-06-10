public class Estudante extends Pessoa {
    private String curso;

    public Estudante(String nome, int idade, String curso) {
        super(nome, idade);
        this.curso = curso;
    }

    public Estudante(String nome, String curso) {
        super(nome); // Chamando o novo construtor da superclasse
        this.curso = curso;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    @Override
    public void exibirInformacoes() {
        super.exibirInformacoes();
        System.out.println("Curso: " + curso);
    }

    public static void main(String[] args) {
        Estudante estudante = new Estudante("Ana", 20, "Engenharia");

        estudante.exibirInformacoes();

        estudante.setNome("Alex");
        estudante.setIdade(24);
        estudante.setCurso("Engenheiro de software");

        estudante.exibirInformacoes();
    }
}
