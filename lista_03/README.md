# psc_03

**_Lista 03_**

Instruções

**Os exercícios desta lista deverão ser entergeus implementados em Java**

Os exercícios deverão ser postados em um repositório GitHub do aluno e o endereço adiciona nos comentários desta entrega.

**Exercícios**

Exercício 1: Criando uma Classe Simples
Objetivo: Criar uma classe simples chamada Pessoa com atributos privados e métodos públicos para acessar e modificar esses atributos.
• Crie uma classe chamada Pessoa.
• Adicione os atributos privados nome (String) e idade (int).
• Crie um construtor que inicialize esses atributos.
• Adicione métodos getNome, setNome, getIdade e setIdade.

Exercício 2: Criando Métodos na Classe
Objetivo: Adicionar métodos na classe Pessoa para exibir informações.
• Adicione um método exibirInformacoes na classe Pessoa que exiba o nome e a idade da pessoa.

Exercício 3: Criando uma Subclasse
Objetivo: Criar uma subclasse Estudante que herde de Pessoa.
• Crie uma classe Estudante que herde da classe Pessoa.
• Adicione um atributo privado curso (String).
• Crie um construtor que inicialize os atributos da superclasse e o novo atributo curso.
• Adicione métodos getCurso e setCurso.

Exercício 4: Sobrescrita de Métodos
Objetivo: Sobrescrever métodos na subclasse Estudante.
• Sobrescreva o método exibirInformacoes na classe Estudante para exibir também o curso do estudante.

Exercício 5: Criando uma Classe com Atributos Protegidos
Objetivo: Criar uma classe Funcionario com atributos protegidos e derivar uma subclasse Gerente.
• Crie uma classe Funcionario com atributos protegidos salario (double) e departamento (String).
• Adicione um método exibirInformacoes na classe Funcionario para exibir as informações.
• Crie uma subclasse Gerente que herde de Funcionario.
• Adicione um atributo privado bonus (double) na classe Gerente.
• Crie um construtor que inicialize os atributos de Funcionario e Gerente.

Exercício 6: Sobrecarga de Construtores
Objetivo: Implementar sobrecarga de construtores na classe Pessoa.
• Adicione um construtor adicional na classe Pessoa que inicialize apenas o nome.
• No construtor que inicializa apenas o nome, defina a idade como 0 por padrão.
• Atualize a classe Estudante para usar o novo construtor de Pessoa, quando necessário.

Exercício 7: Trabalhando com Interfaces
Objetivo: Criar uma interface Trabalhador e implementá-la na classe Funcionario.
• Crie uma interface Trabalhador com um método trabalhar.
• Implemente a interface Trabalhador na classe Funcionario.
• Na implementação do método trabalhar, exiba uma mensagem indicando que o funcionário está trabalhando.
• Atualize a classe Gerente para também implementar a interface Trabalhador.

Exercício 8: Polimorfismo com Interfaces
Objetivo: Demonstrar o polimorfismo usando a interface Trabalhador.
• Crie uma classe Empresa com um método adicionarTrabalhador que receba um objeto do tipo Trabalhador.
• No método adicionarTrabalhador, chame o método trabalhar.
• Crie objetos de Funcionario e Gerente e adicione-os à empresa, demonstrando o polimorfismo.

Exercício 9: Polimorfismo com Classes
Objetivo: Demonstrar o polimorfismo usando classes.
• Crie uma lista de objetos do tipo Pessoa.
• Adicione objetos Pessoa e Estudante na lista.
• Itere sobre a lista e chame o método exibirInformacoes para cada objeto, demonstrando o polimorfismo.

Exercício 10: Classe Abstrata
Objetivo: Criar uma classe abstrata Veiculo e derivar subclasses Carro e Moto.
• Crie uma classe abstrata Veiculo com um método abstrato mover.
• Crie as classes Carro e Moto que herdem de Veiculo.
• Implemente o método mover em ambas as classes, exibindo mensagens apropriadas para cada tipo de veículo.
• Crie uma lista de objetos do tipo Veiculo e adicione objetos Carro e Moto na lista.
• Itere sobre a lista e chame o método mover para cada objeto, demonstrando o polimorfismo.
Esses exercícios vão te guiar através dos principais conceitos de orientação a objetos em Java, desde a criação de classes básicas até a implementação de herança, interfaces, polimorfismo e classes abstratas.
