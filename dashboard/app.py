import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title='AWS Economic Analytics',
    page_icon='📊',
    layout='wide'
)

DB_PATH = Path('data/economic_analytics.db')

@st.cache_resource
def conectar_banco():
    try:
        return sqlite3.connect(str(DB_PATH))
    except Exception as e:
        st.error(f'Erro ao conectar: {e}')
        return None

@st.cache_data
def carregar_dados(tabela):
    try:
        conn = conectar_banco()
        df = pd.read_sql_query(f'SELECT * FROM {tabela} ORDER BY data DESC', conn)
        df['data'] = pd.to_datetime(df['data'])
        return df
    except Exception as e:
        st.error(f'Erro ao carregar {tabela}: {e}')
        return None

# Header
st.markdown('# 📊 AWS Economic Analytics')
st.markdown('Dashboard interativo de indicadores econômicos brasileiros')
st.divider()

# Sidebar
with st.sidebar:
    st.header('⚙️ Configurações')
    
    periodo = st.selectbox(
        'Período',
        ['Último mês', 'Últimos 3 meses', 'Últimos 6 meses', 'Último ano', 'Todo']
    )
    
    dias_map = {
        'Último mês': 30,
        'Últimos 3 meses': 90,
        'Últimos 6 meses': 180,
        'Último ano': 365,
        'Todo': None
    }
    dias = dias_map[periodo]
    
    st.divider()
    st.subheader('Indicadores')
    mostrar_selic = st.checkbox('Selic', value=True)
    mostrar_ipca = st.checkbox('IPCA', value=True)
    mostrar_dolar = st.checkbox('Dólar', value=True)

# Carregar dados
dados = {}

if mostrar_selic:
    df_selic = carregar_dados('selic')
    if df_selic is not None:
        if dias:
            df_selic = df_selic[df_selic['data'] >= datetime.now() - timedelta(days=dias)]
        dados['selic'] = df_selic

if mostrar_ipca:
    df_ipca = carregar_dados('ipca')
    if df_ipca is not None:
        if dias:
            df_ipca = df_ipca[df_ipca['data'] >= datetime.now() - timedelta(days=dias)]
        dados['ipca'] = df_ipca

if mostrar_dolar:
    df_dolar = carregar_dados('dolar')
    if df_dolar is not None:
        if dias:
            df_dolar = df_dolar[df_dolar['data'] >= datetime.now() - timedelta(days=dias)]
        dados['dolar'] = df_dolar

if not dados:
    st.warning('Nenhum indicador selecionado')
    st.stop()

# KPIs
st.header('📈 Indicadores Principais')
cols = st.columns(len(dados))

for idx, (nome, df) in enumerate(dados.items()):
    with cols[idx]:
        valor = df['valor'].iloc[0]
        mudanca = ((df['valor'].iloc[0] - df['valor'].iloc[1]) / df['valor'].iloc[1] * 100) if len(df) > 1 else 0
        st.metric(nome.upper(), f'{valor:.2f}', f'{mudanca:+.2f}%')

st.divider()

# Gráficos
st.header('📊 Análise de Série Temporal')

for nome, df in dados.items():
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['data'], y=df['valor'],
            mode='lines', name='Valor',
            line=dict(color='blue', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=df['data'], y=df['media_movel_30d'],
            mode='lines', name='MM 30d',
            line=dict(color='red', width=1, dash='dash')
        ))
        fig.update_layout(title=f'Evolução - {nome.upper()}', height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.bar(df, x='data', y='variacao_diaria', 
                     title=f'Variação Diária - {nome.upper()}',
                     color='variacao_diaria',
                     color_continuous_scale=['red', 'lightgray', 'green'])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

st.divider()

# Dados brutos
st.header('📋 Dados Brutos')

tabs = st.tabs([f'{nome.upper()} ({len(df)})' for nome, df in dados.items()])

for tab, (nome, df) in zip(tabs, dados.items()):
    with tab:
        st.dataframe(df.head(50), use_container_width=True)

# Rodapé
st.divider()
st.markdown(
    '<div style=\"text-align: center; color: #666;\">'
    'AWS Economic Analytics | Dashboard v1.0'
    '</div>',
    unsafe_allow_html=True
)
