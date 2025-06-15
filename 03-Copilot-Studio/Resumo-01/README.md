# Resumo: Power Platform e Copilot Studio

## Copilot Studio
- **Copilot Baseado em Modelo**: Usa templates pré-definidos para criação rápida de assistentes virtuais (ex: atendimento ao cliente)
- **Copilot Baseado em Descrição com IA**: Gera automaticamente a partir de descrição textual usando IA generativa
- **Copilot em Branco**: Criação manual completa com personalização total de fluxos e integrações

## Ambientes na Power Platform
- **Função**: Isolar recursos por equipe/fase de desenvolvimento (dev/test/prod)
- **Acesso**: Gerenciado via [Centro de Administração](https://admin.powerplatform.microsoft.com)
- **Tipos**: 
  - Padrão (Standard)
  - Avaliação (Trial)
  - Sandbox

## Criando Novo Ambiente
1. Acessar Centro de Administração
2. Definir:
   - Nome
   - Região
   - Tipo de ambiente
3. Vincular banco de dados (Dataverse)
4. Configurar políticas de backup (para ambientes Production)

## Soluções
- **Conceito**: Pacotes que agrupam componentes personalizados
- **Componentes**: Apps, fluxos, tabelas, conectores
- **Tipos**:
  - Não Gerenciadas (editáveis durante desenvolvimento)
  - Gerenciadas (versão final para produção)

## Criando Nova Solução
1. Acessar [Maker Portal](https://make.powerapps.com)
2. Solutions > New solution
3. Definir:
   - Nome
   - Editor
   - Versão
4. Adicionar componentes existentes ou criar novos

## Power Platform Pipelines
- **Objetivo**: Automatizar implantação entre ambientes (dev → test → prod)
- **Configuração**:
  1. Instalar extensão nos ambientes
  2. Definir estágios de implantação
  3. Mapear conexões (Deployment Settings)
- **Fluxo**:
  ```mermaid
  graph LR;
    A[Validar Solução] --> B[Exportar Pacote];
    B --> C[Importar para Ambiente-Alvo];
    C --> D[Testar e Aprovar];
  ```