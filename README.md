# 📊 AWS Economic Analytics

<div align="center">

[![Tests](https://github.com/Miranda-Vers/AWS-Economic-Analytics/actions/workflows/tests.yml/badge.svg)](https://github.com/Miranda-Vers/AWS-Economic-Analytics/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Cloud-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)](https://github.com/psf/black)

**Plataforma completa de Engenharia de Dados para análise econômica do Brasil**

[🚀 Quick Start](#-quick-start) • [📚 Documentação](#-documentação) • [🎯 Features](#-features) • [🛠️ Tecnologias](#-tecnologias)

</div>

---

## 📖 Sobre o Projeto

**AWS Economic Analytics** é uma solução end-to-end de engenharia de dados que automatiza a coleta, processamento e visualização de indicadores econômicos brasileiros. O projeto demonstra competências profissionais em:

- 🔄 **Pipeline ETL** robusto e escalável
- ☁️ **Computação em Nuvem** com AWS S3
- 📊 **Análise de Dados** com Pandas e NumPy
- 📈 **Visualização** interativa com Streamlit e Plotly
- 🐍 **Python Profissional** com boas práticas
- 🔐 **Segurança** e tratamento de erros

---

## 🎯 Features

<table>
<tr>
<td width="50%">

### 💾 Extração de Dados
- ✅ Integração com API SGS (Banco Central)
- ✅ Coleta automatizada de múltiplos indicadores
- ✅ Tratamento robusto de erros
- ✅ Logging estruturado

</td>
<td width="50%">

### ⚙️ Processamento de Dados
- ✅ Limpeza e validação automática
- ✅ Cálculo de indicadores derivados
- ✅ Médias móveis (7, 30 dias)
- ✅ Volatilidade e variações percentuais

</td>
</tr>
<tr>
<td width="50%">

### ☁️ Armazenamento em Nuvem
- ✅ Upload automático para AWS S3
- ✅ Versionamento de arquivos
- ✅ Banco SQLite local
- ✅ Organização em pastas

</td>
<td width="50%">

### 📊 Dashboard Interativo
- ✅ Visualizações com Plotly
- ✅ Filtro por período
- ✅ KPIs em destaque
- ✅ Interface responsiva

</td>
</tr>
</table>

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                   API SGS - Banco Central                       │
└───────────────────────┬─────────────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  📥 EXTRAÇÃO (extract.py)         │
        │  • Requisições HTTP               │
        │  • Validação de dados             │
        │  • Tratamento de erros            │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  📁 AWS S3 (Raw Data)             │
        │  • Backup dos dados brutos        │
        │  • Versionamento                  │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  ⚙️  TRANSFORMAÇÃO (transform.py) │
        │  • Limpeza de dados               │
        │  • Cálculo de indicadores         │
        │  • Médias móveis                  │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  💾 SQLite (Banco Local)          │
        │  • Dados processados              │
        │  • Índices otimizados             │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  ☁️  AWS S3 (Processed Data)      │
        │  • Backup processado              │
        │  • Pronto para BI tools           │
        └───────────────┬───────────────────┘
                        │
                        ▼
        ┌───────────────────────────────────┐
        │  📊 DASHBOARD (dashboard/app.py) │
        │  • Streamlit App                  │
        │  • Gráficos interativos           │
        │  • Filtros por período            │
        └───────────────────────────────────┘
```

---

## 🛠️ Tecnologias

| Categoria | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|----------|
| **Linguagem** | Python | 3.9+ | Programação |
| **Processamento** | Pandas | 2.1.4 | Manipulação de dados |
| **Numérico** | NumPy | 1.24.3 | Cálculos vetorizados |
| **HTTP** | Requests | 2.31.0 | Requisições API |
| **Cloud** | Boto3 | 1.28.85 | Integração AWS |
| **Visualização** | Streamlit | 1.30.0 | Dashboard web |
| **Gráficos** | Plotly | 5.18.0 | Gráficos interativos |
| **Config** | python-dotenv | 1.0.0 | Variáveis de ambiente |
| **Testes** | Pytest | 7.4.3 | Testes unitários |

---

## 📚 Indicadores Disponíveis

| Indicador | Código SGS | Descrição | Período |
|-----------|-----------|-----------|---------|
| 📈 **Taxa Selic** | 432 | Taxa média de juros overnight | Diário |
| 💰 **IPCA** | 433 | Índice de Preços ao Consumidor Amplo | Mensal |
| 💵 **Câmbio USD/BRL** | 1 | Taxa de câmbio nominal média | Diário |

---

## 🚀 Quick Start

### 1️⃣ Pré-requisitos

```bash
# Verificar versões
python --version          # 3.9+
pip --version            # Atualizado
git --version            # Instalado
aws --version            # (Opcional para S3)
```

### 2️⃣ Clonar e Configurar

```bash
# Clonar repositório
git clone https://github.com/Miranda-Vers/AWS-Economic-Analytics.git
cd AWS-Economic-Analytics

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
# Windows:
.\venv\Scripts\Activate.ps1

# Linux/macOS:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3️⃣ Configurar Variáveis de Ambiente

```bash
# Copiar exemplo
cp .env.example .env

# Editar com suas credenciais AWS (opcional)
# AWS_ACCESS_KEY_ID=sua_chave
# AWS_SECRET_ACCESS_KEY=sua_senha
# S3_BUCKET_NAME=seu-bucket
```

### 4️⃣ Executar Pipeline

```bash
# 1. Extrair dados do Banco Central
python scripts/extract.py

# 2. Transformar e processar
python scripts/transform.py

# 3. Upload para AWS S3 (opcional)
python scripts/upload_s3.py

# 4. Visualizar dashboard
streamlit run dashboard/app.py
```

O dashboard abrirá em: **http://localhost:8501**

---

## 📁 Estrutura do Projeto

```
AWS-Economic-Analytics/
│
├── 📄 README.md                 ← Documentação principal
├── 📄 QUICKSTART.md             ← Guia rápido
├── 📄 CHANGELOG.md              ← Histórico de versões
├── 📄 LICENSE                   ← Licença MIT
├── 📄 requirements.txt          ← Dependências Python
├── 📄 .env.example              ← Variáveis de exemplo
├── 📄 .gitignore                ← Arquivos ignorados
│
├── 📁 scripts/
│   ├── extract.py               ← 📥 Coleta dados da API
│   ├── transform.py             ← ⚙️ Processa e transforma
│   ├── upload_s3.py             ← ☁️ Upload para AWS S3
│   └── test_api.py              ← ✅ Testes da API
│
├── 📁 dashboard/
│   └── app.py                   ← 📊 Dashboard Streamlit
│
├── 📁 data/
│   ├── raw/                     ← 📦 Dados brutos da API
│   │   ├── selic.csv
│   │   ├── ipca.csv
│   │   └── dolar.csv
│   └── processed/               ← ✨ Dados processados
│       └── .gitkeep
│
├── 📁 tests/
│   ├── test_structure.py        ← ✅ Testes de estrutura
│   └── __init__.py
│
└── 📁 .github/
    └── workflows/
        └── tests.yml            ← 🔄 CI/CD automático
```

---

## 📖 Como Usar

### 🔹 Extrair Dados

```bash
python scripts/extract.py
```

**O que faz:**
- Conecta na API do Banco Central
- Coleta os 3 indicadores
- Salva em `data/raw/*.csv`
- Exibe relatório com logging

### 🔹 Processar Dados

```bash
python scripts/transform.py
```

**O que faz:**
- Limpa e valida os dados
- Calcula variações percentuais
- Calcula médias móveis (7, 30 dias)
- Calcula volatilidade
- Salva em SQLite (`data/economic_analytics.db`)
- Salva CSVs processados em `data/processed/`

### 🔹 Upload para AWS S3

```bash
python scripts/upload_s3.py
```

**O que faz:**
- Faz upload dos CSVs processados
- Faz upload do banco SQLite
- Organiza em pastas: `dados-processados/` e `banco-dados/`

**Pré-requisitos:**
```bash
aws configure  # Configure suas credenciais
```

### 🔹 Visualizar Dashboard

```bash
streamlit run dashboard/app.py
```

**Features:**
- 📊 Gráficos de série temporal
- 📈 Gráficos de variação diária
- 🎨 KPIs em destaque
- 🔍 Filtro por período (1m, 3m, 6m, 1a, todo)
- 📋 Dados brutos em abas
- 📱 Interface responsiva

---

## 🔧 Configuração AWS S3 (Opcional)

### 1. Instalar AWS CLI

```bash
# Windows (Chocolatey)
choco install awscli

# macOS (Homebrew)
brew install awscli

# Ou download direto: https://aws.amazon.com/cli/
```

### 2. Configurar Credenciais

```bash
aws configure
# AWS Access Key ID: [sua-chave]
# AWS Secret Access Key: [sua-senha]
# Default region: us-east-1
# Default output: json
```

### 3. Criar Bucket S3

```bash
aws s3 mb s3://economic-analytics-seu-nome --region us-east-1
```

### 4. Atualizar `.env`

```env
AWS_ACCESS_KEY_ID=sua_chave
AWS_SECRET_ACCESS_KEY=sua_senha
S3_BUCKET_NAME=economic-analytics-seu-nome
```

### 5. Executar Upload

```bash
python scripts/upload_s3.py
```

---

## ✅ Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=scripts --cov-report=html

# Teste específico
pytest tests/test_structure.py::test_scripts_exist -v
```

---

## 📊 Exemplo de Saída

### Extração
```
✅ Dados extraídos com sucesso!
- selic.csv: 2500 registros
- ipca.csv: 150 registros
- dolar.csv: 2500 registros
```

### Transformação
```
📊 Calculando indicadores...
✓ selic: 2500 registros processados
✓ ipca: 150 registros processados
✓ dolar: 2500 registros processados

💾 Banco SQLite criado: data/economic_analytics.db
```

### Dashboard
```
🚀 Streamlit app running on http://localhost:8501
```

---

## 🗺️ Roadmap

### ✅ Concluído (v1.0.0)
- [x] Pipeline ETL completo
- [x] Integração API Banco Central
- [x] Dashboard Streamlit
- [x] Upload AWS S3
- [x] Testes automáticos
- [x] GitHub Actions CI/CD
- [x] Documentação profissional

### 🚧 Em Desenvolvimento
- [ ] Integração AWS Glue
- [ ] Consultas com Athena
- [ ] PostgreSQL em produção
- [ ] Sistema de alertas

### 📋 Planejado
- [ ] API REST com FastAPI
- [ ] Deploy em AWS ECS
- [ ] Mais indicadores econômicos
- [ ] Previsões com ML (ARIMA, Prophet)
- [ ] Integração Metabase/Superset
- [ ] Docker + docker-compose

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Crie uma branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'feat: adicionar MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. **Abra um Pull Request**

### Padrões de Código
- Seguir [PEP 8](https://pep8.org/)
- Adicionar docstrings em funções
- Testes para novas features
- Type hints quando possível

---

## 📝 Licença

Este projeto está licenciado sob a Licença **MIT** - veja [LICENSE](LICENSE) para detalhes.

```
MIT License - Você pode usar, modificar e distribuir este projeto livremente
```

---

## 👨‍💻 Autor

<div align="center">

**Desenvolvido por [Miranda-Vers](https://github.com/Miranda-Vers)**

Projeto de portfólio demonstrando competências em:
- Engenharia de Dados
- Python Profissional
- AWS e Cloud Computing
- Análise e Visualização de Dados

</div>

---

## 📞 Suporte

<div align="center">

| Recurso | Link |
|---------|------|
| **Issues** | [Abrir uma issue](https://github.com/Miranda-Vers/AWS-Economic-Analytics/issues) |
| **Discussions** | [Discussões](https://github.com/Miranda-Vers/AWS-Economic-Analytics/discussions) |
| **Documentação** | [Wiki](https://github.com/Miranda-Vers/AWS-Economic-Analytics/wiki) |

</div>

---

## 🌟 Status do Projeto

[![GitHub Stars](https://img.shields.io/github/stars/Miranda-Vers/AWS-Economic-Analytics?style=social)](https://github.com/Miranda-Vers/AWS-Economic-Analytics)
[![GitHub Forks](https://img.shields.io/github/forks/Miranda-Vers/AWS-Economic-Analytics?style=social)](https://github.com/Miranda-Vers/AWS-Economic-Analytics/fork)
[![GitHub Issues](https://img.shields.io/github/issues/Miranda-Vers/AWS-Economic-Analytics)](https://github.com/Miranda-Vers/AWS-Economic-Analytics/issues)

**✅ Ativo em desenvolvimento contínuo**

---

<div align="center">

**[⬆ Voltar ao topo](#-aws-economic-analytics)**

Por [Miranda-Vers](https://github.com/Miranda-Vers)

</div>