# 📚 Laboratório Azure Speech & Language Studio

Este repositório apresenta as notas, insights e aprendizados adquiridos no laboratório prático envolvendo o **Azure Speech Studio** e o **Azure Language Studio**. O foco foi aprofundar habilidades em análise de fala e linguagem natural, criando soluções de IA voltadas para voz e linguagem.

---

## 🎯 Objetivo do Laboratório
- **Explorar ferramentas de voz e linguagem natural** no Azure (Speech e Language Studio).
- **Desenvolver habilidades práticas** para criar soluções baseadas em IA com foco em fala e texto.
- Organizar anotações e insights num repositório útil para estudos futuros e implementações reais.

---

## 🧩 Conteúdo

1. **Fundamentos de IA Generativa**  
   - Criação de conteúdo (texto, voz, tradução) a partir de instruções em linguagem natural.

2. **Conceitos Fundamentais de IA**  
   - Visão geral da arquitetura, aprendizado de máquina, modelos transformadores e uso responsável da IA.

3. **Fundamentos de Aprendizado de Máquina**  
   - Etapas: coleta de dados, treinamento, avaliação, validação e deploy.

4. **Conceitos de Processamento de Linguagem Natural (NLP)**  
   - Detecção de idioma, extração de entidades, análise de sentimento, sumarização, PII, question answering, CLU.

5. **Análise de Texto e Resposta a Perguntas**  
   - Exercícios com QnA Maker, identificação de entidades e fluxos de intencionalidade no Language Studio :contentReference.

6. **Serviço de Bot do Azure**  
   - Configuração de intents, entidades, rotas conversacionais e integração com Speech e Language.

7. **Compreensão da Linguagem Coloquial**  
   - Desenvolvimento de modelos CLU (Conversational Language Understanding) no Language Studio para interpretar instruções naturais :contentReference.

---

## 🔍 Azure Speech Studio

- Interface visual (*no-code*) para projetos como:  
  - **Speech-to-Text** (transcrição em tempo real ou em lote).
  - **Text-to-Speech** com vozes personalizadas e neural custom voice.
  - **Pronúncia** e **palavra-chave personalizada**, além de tradução.

- Ferramentas testadas: transcrição de áudio, síntese de fala ("speaking clock"), pronúncia e tradução de voz.

---

## 🧠 Azure Language Studio

- UI interativa para usar NLP sem codificação.
- Recursos explorados:
  - **Extração de entidades (NER)** e reconhecimento de PII.
  - **Detecção de idioma**, **key‑phrase extraction**, **sentiment analysis** e *entity linking*.
  - **Question Answering** e CLU para criar bots que compreendem comandos simples (ex: “acender a luz”).

---

## 🚧 Serviço de Bot & Integração

- Integração de Speech e Language com bot frameworks para criar assistentes de voz/texto.
- Fluxos exemplares:
  - Voz → transcrição (Speech Studio) → interpretação de intenção (Language Studio) → resposta verbal (Text-to-Speech).

---

## 🧪 Práticas Realizadas

- **Speech-to-Text**: testes de transcrição em tempo real e em lote.  
- **Text-to-Speech**: síntese de voz com custom voice para criar relógio falante.  
- **Pronúncia e palavra-chave personalizada** usando demos do Speech Studio.  
- **NLP no Language Studio**: extração de entidades, análise de sentimentos e criação de intents.  
- **CLU**: compreensão de linguagem natural (ex: controlar dispositivos).

---

## ✍️ Insights & Notas

- Studios facilitam uso de IA sem código, acelerando a prototipagem.
- Integração entre Speech e Language é eficiente para construção de bots multimodais.
- CLU torna os bots mais humanos, interpretando comandos falados ou digitados.
- Modelos customizados (voz, entidade, intent) trazem personalização essencial em soluções reais.
- Parâmetros de qualidade, controle de viés e segurança são fundamentais para produção.

---

## 🏁 Conclusão

Este laboratório foi fundamental para:  
- Dominar ferramentas Speech e Language Studio.  
- Compreender o fluxo completo de voz → texto → entendimento → resposta.  
- Ampliar a visão sobre IA generativa, ML e NLP no contexto do Azure.  
- Criar um ambiente de estudo organizando anotações e exemplos práticos.