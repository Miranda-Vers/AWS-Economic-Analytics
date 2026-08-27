import pandas as pd
import sqlite3
from pathlib import Path
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DATA_RAW = Path('data/raw')
DATA_PROCESSED = Path('data/processed')
DB_PATH = Path('data/economic_analytics.db')
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

def limpar_dados():
    logger.info('🔄 Limpando dados brutos...')
    dados_brutos = {}
    for arquivo in DATA_RAW.glob('*.csv'):
        nome = arquivo.stem
        try:
            df = pd.read_csv(arquivo)
            if 'data' in df.columns:
                df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
            if 'valor' in df.columns:
                df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
            df_limpo = df.dropna()
            dados_brutos[nome] = df_limpo
            logger.info(f'✓ {nome}: {len(df_limpo)} registros')
        except Exception as e:
            logger.error(f'✗ Erro em {arquivo}: {e}')
    return dados_brutos

def calcular_indicadores(dados):
    logger.info('📊 Calculando indicadores...')
    indicadores = {}
    for nome, df in dados.items():
        df = df.sort_values('data')
        df['variacao_diaria'] = df['valor'].pct_change() * 100
        df['variacao_30d'] = df['valor'].pct_change(30) * 100
        df['media_movel_7d'] = df['valor'].rolling(7, min_periods=1).mean()
        df['media_movel_30d'] = df['valor'].rolling(30, min_periods=1).mean()
        df['volatilidade_7d'] = df['valor'].rolling(7, min_periods=1).std()
        df['volatilidade_30d'] = df['valor'].rolling(30, min_periods=1).std()
        indicadores[nome] = df
    logger.info('✓ Indicadores calculados')
    return indicadores

def salvar_sqlite(dados, db_path):
    logger.info(f'💾 Salvando em {db_path}...')
    try:
        if db_path.exists():
            db_path.unlink()
        conn = sqlite3.connect(db_path)
        for nome, df in dados.items():
            df['data'] = df['data'].astype(str)
            df.to_sql(nome, conn, if_exists='replace', index=False)
            logger.info(f'✓ Tabela {nome} criada')
        metadados = pd.DataFrame({
            'serie': list(dados.keys()),
            'data_atualizacao': [datetime.now().isoformat()] * len(dados),
            'registros': [len(df) for df in dados.values()]
        })
        metadados.to_sql('metadados', conn, if_exists='replace', index=False)
        conn.close()
        logger.info('✅ Banco criado!')
    except Exception as e:
        logger.error(f'❌ Erro: {e}')
        raise

def salvar_csv_processados(dados):
    logger.info('📁 Salvando CSVs...')
    for nome, df in dados.items():
        df['data'] = df['data'].astype(str)
        arquivo = DATA_PROCESSED / f'{nome}_processado.csv'
        df.to_csv(arquivo, index=False)
        logger.info(f'✓ {arquivo}')

def main():
    logger.info('='*60)
    logger.info('TRANSFORMAÇÃO DE DADOS')
    logger.info('='*60 + '\n')
    try:
        dados_limpos = limpar_dados()
        if not dados_limpos:
            logger.error('Nenhum CSV em data/raw')
            return
        dados_processados = calcular_indicadores(dados_limpos)
        salvar_sqlite(dados_processados, DB_PATH)
        salvar_csv_processados(dados_processados)
        logger.info('\n' + '='*60)
        logger.info('✅ TRANSFORMAÇÃO CONCLUÍDA!')
        logger.info('='*60)
    except Exception as e:
        logger.error(f'\n❌ ERRO: {e}')
        raise

if __name__ == '__main__':
    main()
