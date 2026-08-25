# MacroVision

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Cloud-FF9900?style=flat-square&logo=amazon-aws)](https://aws.amazon.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

Pipeline de dados econômicos desenvolvido em Python com armazenamento em AWS para coletar, processar e visualizar indicadores macroeconômicos brasileiros em dashboards interativos.

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Características](#características)
- [Arquitetura](#arquitetura)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Fluxo de Dados](#fluxo-de-dados)
- [Roadmap](#roadmap)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Visão Geral

MacroVision é uma aplicação completa de engenharia de dados que automatiza a coleta de indicadores econômicos brasileiros fornecidos pelo Banco Central do Brasil através da API SGS, realiza transformações sofisticadas e disponibiliza visualizações interativas em tempo real.

O projeto demonstra competências práticas em:

- **Engenharia de Dados**: Pipelines ETL robustos e escaláveis
- **Computação em Nuvem**: Integração com serviços AWS (S3)
- **Processamento de Dados**: Transformações e análises com Pandas
- **Visualização**: Dashboards interativos com Streamlit
- **DevOps**: Versionamento, documentação e boas práticas

## Características

✅ Coleta automatizada de dados da API SGS do Banco Central  
✅ Armazenamento em nuvem com AWS S3  
✅ Transformações de dados com validação de qualidade  
✅ Banco de dados SQLite para persistência local  
✅ Dashboards interativos com Streamlit  
✅ Indicadores calculados: Taxa Selic, IPCA, Câmbio USD/BRL  
✅ Cálculos de variação percentual e médias móveis  
✅ Tratamento de erros e logging estruturado  

## Arquitetura

```
┌─────────────────────┐
│ Banco Central (SGS) │
└──────────┬──────────┘
           │
           ▼
    ┌─────────────┐
    │   Python    │
    │  + Requests │
    └──────┬──────┘
           │
           ▼
    ┌───────────────┐
    │ AWS S3 (Raw)  │
    └──────┬────────┘
           │
           ▼
    ┌──────────────────┐
    │ Pandas Transform │
    └──────┬───────────┘
           │
           ▼
    ┌────────────┐
    │  SQLite    │
    └──────┬─────┘
           │
           ▼
    ┌──────────────┐
    │  Streamlit   │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │  Dashboard   │
    └──────────────┘
```

## Tecnologias

| Categoria | Tecnologia |
|-----------|-----------|
| **Linguagem** | Python 3.9+ |
| **Processamento** | Pandas, NumPy |
| **HTTP** | Requests |
| **Cloud Storage** | AWS S3 + Boto3 |
| **Banco de Dados** | SQLite |
| **Visualização** | Streamlit |
| **Versionamento** | Git/GitHub |

## Pré-requisitos

Antes de começar, certifique-se de que você tem instalado:

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Conta AWS (para usar S3)
- Credenciais AWS configuradas localmente

### Configurar credenciais AWS

```bash
aws configure
```

Ou defina as variáveis de ambiente:

```bash
export AWS_ACCESS_KEY_ID=seu_access_key
export AWS_SECRET_ACCESS_KEY=sua_secret_key
export AWS_REGION=us-east-1
```

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/macrovision.git
cd macrovision
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais AWS:

```env
AWS_ACCESS_KEY_ID=sua_chave
AWS_SECRET_ACCESS_KEY=sua_senha
AWS_REGION=us-east-1
S3_BUCKET_NAME=seu-bucket-macrovision
DATABASE_PATH=data/macrovision.db
```

## Uso

### Executar a extração de dados

Coleta dados da API SGS do Banco Central e armazena no S3:

```bash
python scripts/extract.py
```

### Executar a transformação de dados

Processa dados brutos, aplica transformações e salva em banco local:

```bash
python scripts/transform.py
```

### Iniciar o dashboard

Executa a aplicação Streamlit na porta padrão (8501):

```bash
streamlit run dashboard/app.py
```

A aplicação abrirá automaticamente em `http://localhost:8501`

### Executar pipeline completo

```bash
python scripts/extract.py && python scripts/transform.py && streamlit run dashboard/app.py
```

## Estrutura do Projeto

```
macrovision/
│
├── data/
│   ├── raw/                 # Dados brutos da API
│   └── processed/           # Dados transformados
│
├── scripts/
│   ├── extract.py          # Coleta dados da API SGS
│   ├── transform.py        # Transformações e limpeza
│   └── upload_s3.py        # Upload para AWS S3
│
├── dashboard/
│   └── app.py              # Aplicação Streamlit
│
├── tests/
│   ├── test_extract.py
│   └── test_transform.py
│
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore              # Arquivos ignorados pelo Git
├── requirements.txt        # Dependências Python
├── README.md               # Este arquivo
└── LICENSE                 # Licença MIT
```

## Fluxo de Dados

### 1️⃣ Extração
Os dados são obtidos diretamente da **API SGS do Banco Central do Brasil**.

```python
# Exemplo: Taxa Selic (código 432)
https://api.bcb.gov.br/dados/series/432/dados
```

### 2️⃣ Armazenamento
Os arquivos brutos em formato JSON são enviados para um **bucket S3** com timestamp para versionamento.

```
s3://seu-bucket/raw/selic/2024-01-15_selic_data.json
```

### 3️⃣ Transformação
Aplicam-se as seguintes operações:

- ✓ Conversão de formatos de data
- ✓ Padronização de tipos de dados
- ✓ Tratamento de valores ausentes
- ✓ Cálculo de variação percentual (diária/mensal)
- ✓ Médias móveis (7, 30 dias)
- ✓ Validação de qualidade

### 4️⃣ Visualização
Os dados processados são indexados em **SQLite** e exibidos em **dashboards interativos** com:

- Gráficos de série temporal
- KPIs e estatísticas
- Comparativas entre indicadores
- Filtros por período

## Indicadores Disponíveis

| Indicador | Código SGS | Descrição |
|-----------|-----------|-----------|
| Taxa Selic | 432 | Taxa média de juros overnight |
| IPCA | 433 | Índice de Preços ao Consumidor Amplo |
| Câmbio USD/BRL | 1 | Taxa de câmbio nominal média |

## Roadmap

### Em Desenvolvimento 🔄
- [ ] Testes unitários completos
- [ ] CI/CD com GitHub Actions
- [ ] Docker e docker-compose

### Planejado 📋
- [ ] Integração com AWS Glue para ETL gerenciado
- [ ] Consultas analíticas com Athena
- [ ] Migração para PostgreSQL
- [ ] Deploy em AWS ECS
- [ ] Sistema de alertas automáticos
- [ ] Integração com mais indicadores econômicos
- [ ] API REST para consumir dados

### Futuro 🚀
- [ ] Previsões com modelos ML (ARIMA, Prophet)
- [ ] Dashboard interativo avançado
- [ ] Integração com ferramentas de BI (Metabase, Superset)

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- Use [PEP 8](https://pep8.org/) para estilo
- Adicione docstrings em funções
- Mantenha testes com cobertura acima de 80%
- Use type hints quando possível

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

Desenvolvido como projeto de portfólio para demonstrar competências em **Engenharia de Dados**, **Python**, **AWS** e **Análise de Dados**.

---

### Suporte

Encontrou um bug ou tem uma sugestão? [Abra uma issue](../../issues) no GitHub.

### Status do Projeto

✅ Ativo e em desenvolvimento contínuo
