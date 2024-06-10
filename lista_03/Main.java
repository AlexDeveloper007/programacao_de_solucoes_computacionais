import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        // Pessoa
        ArrayList<Pessoa> listaPessoas = new ArrayList<>();

        listaPessoas.add(new Pessoa("Luis", 19));
        listaPessoas.add(new Estudante("Alex", 24, "Engenharia de Software"));
        listaPessoas.add(new Pessoa("Maria", 44));
        listaPessoas.add(new Estudante("Carlos", "Engenharia Civil"));

        for (Pessoa pessoa : listaPessoas) {
            pessoa.exibirInformacoes();
            System.out.println();
        }

        // Veiculo

        ArrayList<Veiculo> listaVeiculos = new ArrayList<>();

        listaVeiculos.add(new Carro());
        listaVeiculos.add(new Moto());

        for (Veiculo veiculo : listaVeiculos) {
            veiculo.mover();
        }
    }
}
