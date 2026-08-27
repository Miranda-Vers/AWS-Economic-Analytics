# 🚀 Quick Start - AWS Economic Analytics

## Instalação Rápida

\\\ash
# 1. Clonar repositório
git clone https://github.com/Miranda-Vers/AWS-Economic-Analytics.git
cd AWS-Economic-Analytics

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Copiar arquivo de ambiente
cp .env.example .env
\\\

## Usar o Pipeline

\\\ash
# Extrair dados
python scripts/extract.py

# Transformar dados
python scripts/transform.py

# Visualizar dashboard
streamlit run dashboard/app.py
\\\

## Configurar AWS S3 (Opcional)

\\\ash
aws configure
python scripts/upload_s3.py
\\\

---

**Documentação completa:** Veja [README.md](README.md)
