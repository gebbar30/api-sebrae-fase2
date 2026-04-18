# Motor de Análise de Sentimentos SEBRAE (Fase 2)
API RESTful construída com FastAPI e integrada com modelo de Machine Learning (Random Forest) para análise preditiva de satisfação de clientes do varejo.

## Como Executar o Código Localmente
1. Certifique-se de ter o Python 3.9+ instalado.
2. Instale as dependências executando: `pip install -r requirements.txt`
3. Execute o servidor local rodando o comando: `uvicorn main:app --reload`
4. Acesse o navegador em `http://localhost:8000/docs` para testar as rotas GET e POST via interface do Swagger UI.

## Infraestrutura e Deploy (CI/CD)
Este repositório possui uma pipeline configurada via GitHub Actions. O processo realiza o build de uma imagem Docker e publica no DockerHub automaticamente após a aprovação de um merge na branch `main`. O deploy final para o Heroku está configurado para acionamento manual (`workflow_dispatch`), cumprindo as diretrizes de governança do projeto.