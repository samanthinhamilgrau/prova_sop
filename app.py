import streamlit as st
import pandas as pd

# Carregar o CSV
df = pd.read_csv("MS_Financial Sample.csv", sep=';', engine='python', on_bad_lines='skip')

# Limpar nomes das colunas
df.columns = df.columns.str.strip()

# Função para limpar valores monetários, tratando '-' e valores vazios
def limpar_valor(valor):
    if isinstance(valor, str):
        valor = valor.strip().replace('$', '').replace('.', '').replace(',', '.')
        if valor in ['', '-']:
            return 0.0
        try:
            return float(valor)
        except ValueError:
            return 0.0
    return valor

# Aplicar a função nas colunas numéricas
colunas_monetarias = ['Units Sold', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']
for coluna in colunas_monetarias:
    df[coluna] = df[coluna].apply(limpar_valor)

# Converter datas
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Título
st.title("📊 Análise Financeira - MS Sample")

# Vendas por País
st.subheader("🌍 Vendas Totais por País")
vendas_pais = df.groupby("Country")["Sales"].sum().sort_values(ascending=False)
st.bar_chart(vendas_pais)

# Lucro por Segmento
st.subheader("🏷️ Lucro Total por Segmento")
lucro_segmento = df.groupby("Segment")["Profit"].sum()
st.bar_chart(lucro_segmento)

# Evolução das Vendas ao Longo do Tempo
st.subheader("📅 Evolução das Vendas por Data")
vendas_tempo = df.groupby("Date")["Sales"].sum().sort_index()
st.line_chart(vendas_tempo)

# Produto mais lucrativo
st.subheader("💰 Lucro por Produto")
lucro_produto = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)
st.bar_chart(lucro_produto)
