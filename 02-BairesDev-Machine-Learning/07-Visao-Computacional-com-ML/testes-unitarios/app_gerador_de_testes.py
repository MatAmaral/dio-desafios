import os
import argparse
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def configurar_llm():
    """Configura e retorna uma instância do modelo de linguagem do Azure."""
    try:
        llm = AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-01",  # A versão pode variar, verifique sua configuração no Azure
            azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
            temperature=0.1 # Usamos uma temperatura baixa para obter resultados mais determinísticos e focados
        )
        return llm
    except Exception as e:
        print(f"Erro ao configurar o LLM do Azure: {e}")
        print("Verifique se as variáveis de ambiente AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY e AZURE_OPENAI_CHAT_DEPLOYMENT_NAME estão configuradas corretamente no arquivo .env")
        exit()

def criar_prompt(codigo_fonte):
    """Cria o prompt detalhado para o modelo de linguagem."""
    prompt = f"""
    Você é um especialista em desenvolvimento de software e testes (QA) em Python.
    Sua tarefa é criar um conjunto de testes unitários robustos e completos para o código Python fornecido abaixo.

    Instruções:
    1.  **Framework de Teste:** Utilize o framework `unittest` da biblioteca padrão do Python.
    2.  **Cobertura:** Certifique-se de cobrir os seguintes cenários:
        -   Caminhos felizes (happy paths): entradas válidas que produzem os resultados esperados.
        -   Casos de borda (edge cases): valores extremos, como zeros, números negativos, etc.
        -   Tratamento de erros: testes que verificam se as exceções esperadas (`ValueError`, `TypeError`, `ZeroDivisionError`, etc.) são levantadas corretamente com entradas inválidas.
    3.  **Estrutura:**
        -   Importe o módulo `unittest` e a função/classe a ser testada.
        -   Crie uma classe de teste que herde de `unittest.TestCase`.
        -   Cada cenário de teste deve ser um método separado dentro da classe, com um nome descritivo (ex: `test_soma_positiva`, `test_divisao_por_zero_deve_lancar_excecao`).
    4.  **Formato da Saída:** O resultado deve ser um único bloco de código Python, completo e pronto para ser executado. Não inclua nenhuma explicação, introdução ou texto adicional fora do bloco de código.

    --- CÓDIGO A SER TESTADO ---
    ```python
    {codigo_fonte}
    ```
    --- FIM DO CÓDIGO ---

    Agora, gere o script de teste unitário.
    """
    return prompt

def gerar_testes(llm, codigo_fonte):
    """Envia o prompt para o LLM e retorna o código de teste gerado."""
    prompt = criar_prompt(codigo_fonte)
    mensagem = [HumanMessage(content=prompt)]
    
    print("Enviando solicitação para a API do Azure OpenAI. Isso pode levar alguns segundos...")
    resposta = llm.invoke(mensagem)
    print("Testes gerados com sucesso!")
    
    # Extrai o bloco de código da resposta do modelo
    codigo_gerado = resposta.content.strip()
    if codigo_gerado.startswith("```python"):
        codigo_gerado = codigo_gerado[len("```python"):].strip()
    if codigo_gerado.endswith("```"):
        codigo_gerado = codigo_gerado[:-len("```")].strip()
        
    return codigo_gerado

def salvar_arquivo_teste(caminho_arquivo_original, codigo_teste):
    """Salva o código de teste gerado em um novo arquivo."""
    diretorio, nome_arquivo = os.path.split(caminho_arquivo_original)
    nome_base, extensao = os.path.splitext(nome_arquivo)
    
    # Cria o nome do arquivo de teste
    novo_nome_arquivo = f"test_{nome_base}{extensao}"
    novo_caminho = os.path.join(diretorio, novo_nome_arquivo)
    
    with open(novo_caminho, 'w', encoding='utf-8') as f:
        f.write(codigo_teste)
    
    print(f"Arquivo de teste salvo em: {novo_caminho}")
    return novo_caminho

def main():
    """Função principal que orquestra o processo."""
    parser = argparse.ArgumentParser(description="Gerador Automático de Testes Unitários com LangChain e Azure ChatGPT")
    parser.add_argument("arquivo", help="O caminho para o arquivo Python que contém o código a ser testado.")
    args = parser.parse_args()

    caminho_arquivo = args.arquivo

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo_fonte = f.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return

    # 1. Configurar o LLM
    llm = configurar_llm()

    # 2. Gerar o código de teste
    codigo_teste_gerado = gerar_testes(llm, codigo_fonte)

    # 3. Salvar o código de teste em um novo arquivo
    salvar_arquivo_teste(caminho_arquivo, codigo_teste_gerado)
    
    print("\nProcesso concluído.")
    print(f"Para executar os testes gerados, use o comando: python -m unittest {caminho_arquivo.replace('.py', '_test.py')}")


if __name__ == "__main__":
    main()