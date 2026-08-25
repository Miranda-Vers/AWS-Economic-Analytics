# AWS-Economic-Analytics
Plataforma de análise econômica desenvolvida com Python e AWS para coletar, processar e visualizar indicadores do Banco Central (Selic, IPCA e câmbio) em dashboards interativos.

📊 MacroVision

Pipeline de dados econômicos desenvolvido com Python e AWS para coletar, processar e visualizar indicadores macroeconômicos brasileiros em dashboards interativos.

🚀 Visão Geral

O MacroVision é um projeto de análise de dados econômicos que consome informações públicas do Banco Central do Brasil por meio da API SGS, realiza o tratamento dos dados e disponibiliza visualizações interativas para apoiar análises econômicas.

O objetivo do projeto é demonstrar conhecimentos em:

Engenharia de Dados
Computação em Nuvem (AWS)
Análise de Dados
Visualização de Dados
Boas práticas de desenvolvimento
🏗️ Arquitetura
Banco Central (SGS API)
          │
          ▼
   Python + Requests
          │
          ▼
      AWS S3 (Raw)
          │
          ▼
 Pandas (Transformação)
          │
          ▼
       SQLite
          │
          ▼
      Streamlit
          │
          ▼
      Dashboard
📈 Indicadores Analisados
Taxa Selic
IPCA (Inflação)
Câmbio USD/BRL
⚙️ Tecnologias Utilizadas
Python
Pandas
Requests
AWS S3
Boto3
SQLite
Streamlit
Git
GitHub
📂 Estrutura do Projeto
macrovision/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── upload_s3.py
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
🔄 Fluxo de Dados
1. Extração

Os dados são obtidos da API SGS do Banco Central do Brasil.

2. Armazenamento

Os arquivos brutos são enviados para um bucket Amazon S3.

3. Transformação

O tratamento inclui:

Conversão de datas
Padronização de tipos
Cálculo de variação percentual
Médias móveis
Criação de métricas para análise
4. Visualização

Os dados processados são exibidos em dashboards interativos desenvolvidos com Streamlit.

▶️ Como Executar
Clonar o repositório
git clone https://github.com/seu-usuario/macrovision.git
cd macrovision
Criar ambiente virtual
python -m venv venv
Ativar ambiente

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate
Instalar dependências
pip install -r requirements.txt
Executar ingestão
python scripts/extract.py
Executar transformação
python scripts/transform.py
Iniciar dashboard
streamlit run dashboard/app.py
📌 Possíveis Evoluções
Integração com AWS Glue
Consultas analíticas com Athena
Automatização via AWS Lambda
Banco de dados PostgreSQL
Deploy em AWS ECS ou EC2
Alertas automáticos para mudanças relevantes nos indicadores
🎯 Objetivo do Projeto

Este projeto foi desenvolvido para aplicar conceitos de engenharia de dados e computação em nuvem em um caso real, utilizando indicadores econômicos brasileiros para demonstrar a construção de uma pipeline de dados ponta a ponta.

👨‍💻 Autor

Desenvolvido como projeto de portfólio para demonstrar competências em Python, AWS, análise de dados e visualização de informações.
