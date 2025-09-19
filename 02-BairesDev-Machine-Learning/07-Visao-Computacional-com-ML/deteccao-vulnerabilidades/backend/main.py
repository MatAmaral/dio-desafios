import os
import base64
import tempfile
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Carregar variáveis de ambiente do arquivo .env
env_path = Path(__file__).resolve(strict=True).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Configurar a API key da OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Inicializar o FastAPI e habilitar CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Diretório do frontend 
frontend_path = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/app", StaticFiles(directory=frontend_path, html=True), name="static")

# Função que cria o prompt base
def criar_prompt_modelo_ameacas(tipo_aplicacao, autenticacao, acesso_internet, dados_sensiveis, descricao_aplicacao):
    return f"""Aja como um especialista em cibersegurança com 20 anos de experiência usando o modelo STRIDE.
Tipo de aplicação: {tipo_aplicacao}
Autenticação: {autenticacao}
Exposta na internet? {acesso_internet}
Dados sensíveis: {dados_sensiveis}
Descrição: {descricao_aplicacao}

Forneça ameaças plausíveis em formato JSON com as chaves 'threat_model' e 'improvement_suggestions'.
"""

# Rota principal para análise
@app.post("/analisar_ameacas")
async def analisar_ameacas(
    imagem: UploadFile = File(...),
    tipo_aplicacao: str = Form(...),
    autenticacao: str = Form(...),
    acesso_internet: str = Form(...),
    dados_sensiveis: str = Form(...),
    descricao_aplicacao: str = Form(...)
):
    try:
        # Criar prompt
        prompt = criar_prompt_modelo_ameacas(
            tipo_aplicacao, autenticacao, acesso_internet, dados_sensiveis, descricao_aplicacao
        )

        # Salvar imagem temporariamente
        content = await imagem.read()
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(imagem.filename).suffix) as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name

        # Converter imagem para base64
        with open(temp_file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('ascii')

        # Construir prompt com imagem e texto
        chat_prompt = [
            {"role": "system", "content": "Você é uma IA especialista em cibersegurança e modelagem de ameaças."},
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded_string}"}},
                {"type": "text", "text": "Analise e gere um modelo STRIDE em JSON."}
            ]}
        ]

        # Chamada para o modelo da OpenAI
        # response = openai.chat.completions.create(
        #     model="gpt-3.5-turbo",  # ou "gpt-3.5-turbo" se não tiver acesso a visão
        #     messages=chat_prompt,
        #     max_tokens=1500
        # )
        
        # Chamada com mock para não gastar credito da API KEY
        response = {
                    "choices": [{
                        "message": {
                            "content": """
                    {
                        "threat_model": [
                            {
                            "Threat Type": "Spoofing",
                            "Scenario": "Um atacante se passa por um usuário legítimo e acessa a funcionalidade de anotação sem autenticação forte.",
                            "Potential Impact": "Modificação ou roubo de anotações privadas e comprometimento da integridade dos dados."
                            },
                            {
                            "Threat Type": "Tampering",
                            "Scenario": "Interferência no fluxo entre o sistema de recuperação e o banco de dados local para injetar ou alterar artigos armazenados.",
                            "Potential Impact": "Corrupção de dados, perda de confiabilidade das informações e falhas na recuperação de artigos."
                            },
                            {
                            "Threat Type": "Repudiation",
                            "Scenario": "Usuários realizam buscas ou alterações sem que haja um sistema de logs robusto para rastrear ações.",
                            "Potential Impact": "Impossibilidade de auditar ações maliciosas ou uso indevido do sistema."
                            },
                            {
                            "Threat Type": "Information Disclosure",
                            "Scenario": "Dados sensíveis (como artigos, anotações e histórico de buscas) são transmitidos ou armazenados sem criptografia.",
                            "Potential Impact": "Vazamento de informações acadêmicas ou pessoais, violando políticas de privacidade."
                            },
                            {
                            "Threat Type": "Denial of Service",
                            "Scenario": "Um atacante envia consultas automáticas em massa para o sistema de extensão de consultas via Web.",
                            "Potential Impact": "Sobrecarregamento do sistema e indisponibilidade do serviço legítimo aos usuários."
                            },
                            {
                            "Threat Type": "Elevation of Privilege",
                            "Scenario": "Um usuário comum descobre endpoints administrativos não protegidos e obtém acesso privilegiado.",
                            "Potential Impact": "Controle total sobre dados, configurações do sistema e possível comprometimento da infraestrutura."
                            }
                        ],
                        "improvement_suggestions": [
                            "Especificar claramente os mecanismos de autenticação e controle de acesso entre os módulos.",
                            "Descrever se há criptografia dos dados em repouso e em trânsito, especialmente nos fluxos sensíveis.",
                            "Detalhar como o sistema lida com logs e rastreamento de ações do usuário.",
                            "Indicar as barreiras de proteção entre os componentes internos e a web externa.",
                            "Explicitar se existe algum controle de limite de requisições para evitar DoS."
                        ]
                    }
                """
                        }
                    }]
                }

        # Limpeza do arquivo temporário
        os.remove(temp_file_path)

        # Retornar a resposta do modelo
        # return JSONResponse(content=response.to_dict(), status_code=200)
    
        # Retornar a resposta do mock
        return JSONResponse(content=response, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
