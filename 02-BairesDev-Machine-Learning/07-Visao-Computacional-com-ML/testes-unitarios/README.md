# Desafio: Gerador Automático de Testes Unitários com LangChain e Azure OpenAI

Este projeto é uma solução para o desafio de automatizar a criação de testes unitários em Python, utilizando o poder dos modelos de linguagem (LLMs) através da biblioteca LangChain e do serviço Azure OpenAI (ChatGPT).

## 📝 Descrição do Projeto

O aplicativo é uma ferramenta de linha de comando (CLI) que recebe um arquivo Python como entrada, analisa seu conteúdo e utiliza um modelo de linguagem avançado para gerar um script de testes unitários completo e funcional usando o framework `unittest` do Python. O objetivo é acelerar o ciclo de desenvolvimento, garantir a qualidade do código e demonstrar uma aplicação prática de IA generativa em engenharia de software.

### ✨ Funcionalidades

-   **Automação de Testes**: Gera automaticamente testes para funções e classes Python.
-   **Integração com LLM**: Conecta-se ao Azure OpenAI Service usando LangChain.
-   **Prompt Engineering**: Utiliza um prompt cuidadosamente elaborado para garantir que os testes gerados sejam de alta qualidade, cobrindo casos de sucesso, casos de borda e tratamento de exceções.
-   **Interface Simples**: Ferramenta de linha de comando fácil de usar.
-   **Configuração Segura**: Carrega credenciais de API de forma segura a partir de variáveis de ambiente.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.8+**
-   **LangChain**: Framework para desenvolvimento de aplicações com LLMs.
-   **Azure OpenAI Service**: Serviço de nuvem da Microsoft para acesso a modelos como GPT-4 e GPT-3.5-Turbo.
-   **python-dotenv**: Para gerenciamento de variáveis de ambiente.
-   **unittest**: Biblioteca padrão do Python para testes unitários.

## 🚀 Como Configurar e Executar

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### Pré-requisitos

-   **Python 3.8 ou superior** instalado.
-   Uma conta no **Microsoft Azure** com acesso ao **Azure OpenAI Service**.
-   Um **modelo de chat** (como `gpt-35-turbo` ou `gpt-4`) já implantado (deployed) no seu recurso Azure OpenAI.
-   **Git** instalado para clonar o repositório.

### Passos

1.  **Clone o Repositório**
    ```bash
    git clone https://github.com/Angeloabrita/Gerando-Testes-Unit-rios-com-LangChain-e-Azure-ChatGPT.git
    cd seu-repositorio
    ```

2.  **Crie e Ative um Ambiente Virtual**
    Isso isola as dependências do projeto.

    *   No Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as Dependências**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente**
    O projeto precisa de suas credenciais do Azure para funcionar.

    a. Copie o arquivo de exemplo:
    ```bash
    copy .env.example .env  # No Windows
    # ou
    cp .env.example .env    # No macOS/Linux
    ```

    b. Abra o arquivo `.env` recém-criado e preencha com suas informações do Azure OpenAI:
    ```ini
    AZURE_OPENAI_ENDPOINT="https://SEU-RECURSO.openai.azure.com/"
    AZURE_OPENAI_API_KEY="SUA_CHAVE_DE_API"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="NOME_DA_SUA_IMPLANTACAO_GPT"
    ```

5.  **Execute o Gerador de Testes**
    Use o script `app_gerador_de_testes.py` e passe o caminho do arquivo que você deseja testar como argumento. Para testar o exemplo fornecido:

    ```bash
    python app_gerador_de_testes.py codigo_a_ser_testado/calculadora.py
    ```

    O script irá se comunicar com a API do Azure e, ao final, criará um novo arquivo chamado `test_calculadora.py` dentro da mesma pasta.

      <!-- Opcional: Adicione um screenshot aqui -->

## 📂 Estrutura do Projeto

```
/
├── .gitignore                  # Arquivos e pastas a serem ignorados pelo Git
├── README.md                   # Esta documentação
├── requirements.txt            # Dependências Python do projeto
├── .env.example                # Arquivo de exemplo para variáveis de ambiente
├── app_gerador_de_testes.py    # O script principal da aplicação
└── codigo_a_ser_testado/
    └── calculadora.py          # Um código de exemplo para o qual gerar testes
```

## 🤖 Exemplo de Uso e Resultado

Vamos analisar o exemplo incluído no repositório.

**1. Código de Entrada (`codigo_a_ser_testado/calculadora.py`):**
```python
def calcular(operacao, a, b):
    # ... (código da função)
```

**2. Comando de Execução:**
```bash
python app_gerador_de_testes.py codigo_a_ser_testado/calculadora.py
```

**3. Resultado Gerado (`test_calculadora.py`):**
O LLM irá gerar um arquivo de teste similar a este:

```python
import unittest
from calculadora import calcular

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular('soma', 5, 3), 8)
        self.assertEqual(calcular('soma', -1, 1), 0)
        self.assertAlmostEqual(calcular('soma', 0.1, 0.2), 0.3)

    def test_subtracao(self):
        self.assertEqual(calcular('subtracao', 10, 4), 6)
        self.assertEqual(calcular('subtracao', 5, 10), -5)

    def test_multiplicacao(self):
        self.assertEqual(calcular('multiplicacao', 3, 7), 21)
        self.assertEqual(calcular('multiplicacao', 5, 0), 0)

    def test_divisao(self):
        self.assertEqual(calcular('divisao', 10, 2), 5)
        self.assertAlmostEqual(calcular('divisao', 5, 2), 2.5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calcular('divisao', 10, 0)

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calcular('potencia', 2, 3)

    def test_tipo_de_entrada_invalido(self):
        with self.assertRaises(TypeError):
            calcular('soma', 'a', 3)
        with self.assertRaises(TypeError):
            calcular('soma', 5, 'b')

```

**4. Executando os Testes Gerados:**
Você pode verificar se os testes funcionam com o executor de testes do Python:
```bash
python -m unittest codigo_a_ser_testado/test_calculadora.py
```