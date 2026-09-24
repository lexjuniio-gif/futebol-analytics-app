import streamlit as st
import pandas as pd

# Configuração da página do App
st.set_page_config(page_title="Central de Futebol Global", page_icon="⚽", layout="wide")

st.title("⚽ Central de Inteligência - Futebol Multi-Ligas")
st.markdown("Bem-vindo ao seu painel dinâmico de análise de desempenho e estatísticas.")

# Barra lateral (Sidebar) para controlos dinâmicos
st.sidebar.header("Painel de Controlo")
liga_escolhida = st.sidebar.selectbox(
    "Selecione a Liga:",
    ["Brasileirão", "Bundesliga (Alemanha)", "Campeonato Irlandês", "Campeonato Boliviano"]
)

# Botão de ação dinâmica
if st.sidebar.button("Atualizar Dados da Liga"):
    st.sidebar.success(f"A ligar aos servidores para atualizar {liga_escolhida}...")

# Área Principal do App
st.subheader(f"📊 Painel Analítico: {liga_escolhida}")

# Simulando dados dinâmicos com base na escolha do utilizador
if liga_escolhida == "Brasileirão":
    dados_exemplo = {
        'Equipa': ['Palmeiras', 'Flamengo', 'Internacional', 'Fortaleza', 'São Paulo'],
        'Jogos': [38, 38, 38, 38, 38],
        'Pontos': [73, 68, 65, 65, 59],
        'Aproveitamento (%)': [64.0, 59.6, 57.0, 57.0, 51.7]
    }
elif liga_escolhida == "Bundesliga (Alemanha)":
    dados_exemplo = {
        'Equipa': ['Bayer Leverkusen', 'Bayern de Munique', 'Stuttgart', 'Leipzig', 'Borussia Dortmund'],
        'Jogos': [34, 34, 34, 34, 34],
        'Pontos': [90, 72, 73, 65, 63],
        'Aproveitamento (%)': [88.2, 70.5, 71.5, 63.7, 61.7]
    }
else:
    dados_exemplo = {
        'Equipa': ['Equipa A', 'Equipa B', 'Equipa C', 'Equipa D'],
        'Jogos': [30, 30, 30, 30],
        'Pontos': [65, 58, 52, 45],
        'Aproveitamento (%)': [72.2, 64.4, 57.7, 50.0]
    }

df_app = pd.DataFrame(dados_exemplo)

# Exibindo métricas visuais em destaque (Cards)
col1, col2, col3 = st.columns(3)
col1.metric("Líder Atual", df_app.iloc[0]['Equipa'])
col2.metric("Pontuação do Líder", f"{df_app.iloc[0]['Pontos']} pts")
col3.metric("Aproveitamento", f"{df_app.iloc[0]['Aproveitamento (%)']}%")

# Tabela interativa na tela
st.markdown("### Tabela de Classificação Dinâmica")
st.dataframe(df_app, use_container_width=True)

# Gráfico interativo automático gerado pelo Streamlit
st.markdown("### Gráfico de Desempenho (Pontos por Equipa)")
st.bar_chart(df_app.set_index('Equipa')['Pontos'])