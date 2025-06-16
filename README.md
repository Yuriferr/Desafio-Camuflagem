# 🧬 Simulador de Algoritmo Genético para Descoberta de Cores

Este projeto é uma simulação visual, construída em Python, que utiliza um Algoritmo Genético para "descobrir" uma cor RGB alvo. A cada geração, a população de cores evolui para se aproximar cada vez mais do objetivo, demonstrando visualmente os princípios da seleção natural e da genética computacional.

O painel de controle exibe a cor alvo, a cor mais próxima encontrada pela geração atual e um gráfico em tempo real que mostra a evolução da "aptidão" (fitness) ao longo das gerações.

## 🎯 Funcionalidades

* **Simulação em Tempo Real:** Observe a cor candidata evoluir e se aproximar da cor alvo.
* **Visualização de Dados:** Um gráfico Matplotlib integrado à janela do Pygame exibe a melhoria do fitness a cada geração.
* **Código Modular:** A lógica do Algoritmo Genético (`genetic_algorithm.py`) é separada da lógica de visualização (`main.py`), seguindo boas práticas de programação.
* **Ambiente Configurável:** Altere facilmente parâmetros como tamanho da população e taxa de mutação no arquivo `main.py`.

## 💻 Tecnologias Utilizadas

* **Python 3**
* **Pygame:** Para a criação da janela e a renderização dos elementos visuais.
* **Matplotlib:** Para a geração do gráfico de performance em tempo real.
* **NumPy:** Como dependência do Matplotlib para operações numéricas.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a simulação na sua máquina.

### Pré-requisitos

* [Python 3.8+](https://www.python.org/downloads/) instalado.
* [Git](https://git-scm.com/downloads) instalado para clonar o repositório.

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    Isso cria um ambiente isolado para as dependências do projeto, o que é uma boa prática.
    ```bash
    # Cria o ambiente na pasta .venv
    python -m venv .venv

    # Ativa o ambiente (Windows - PowerShell/Terminal)
    .\.venv\Scripts\Activate.ps1
    
    # (Se usar Git Bash ou Linux/macOS, o comando seria: source .venv/bin/activate)
    ```
    Você saberá que funcionou quando vir `(.venv)` no início da linha do seu terminal.

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a simulação:**
    ```bash
    python main.py
    ```
    A janela do Pygame com a simulação deverá aparecer!

## 📂 Estrutura do Código

* `main.py`: Responsável por toda a parte de visualização com Pygame, o loop principal do programa e a integração do gráfico Matplotlib.
* `genetic_algorithm.py`: Contém a classe `GeneticAlgorithm`, que encapsula toda a lógica da evolução: criação da população, cálculo de fitness, seleção, cruzamento (crossover) e mutação.
* `requirements.txt`: Lista as bibliotecas Python necessárias para o projeto.

## 🧠 Como Funciona o Algoritmo

* **Indivíduo:** Cada "indivíduo" é uma simples cor, representada por uma lista de três valores `[R, G, B]`.
* **População:** Uma coleção de 50 indivíduos (cores) que formam uma geração.
* **Fitness (Aptidão):** A aptidão de um indivíduo é medida pela sua "proximidade" com a cor alvo. Calculamos a distância euclidiana entre as duas cores no espaço 3D RGB e usamos o inverso dessa distância como pontuação de fitness (menor distância = maior aptidão).
* **Evolução:**
    1.  **Seleção:** Indivíduos com maior fitness têm mais chances de serem selecionados para a reprodução.
    2.  **Cruzamento (Crossover):** Dois pais selecionados combinam seus genes (valores R, G e B) para criar um novo filho.
    3.  **Mutação:** Há uma pequena chance de que um dos genes do filho sofra uma pequena alteração aleatória. Isso introduz novidade na população e evita estagnação.
    4.  **Elitismo:** O melhor indivíduo da geração anterior é sempre preservado e passa diretamente para a próxima, garantindo que o progresso nunca seja perdido.

## 📜 Licença

Este projeto está sob a licença MIT.

---