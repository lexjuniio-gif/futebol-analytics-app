import streamlit as st
import pandas as pd

# Configuração da página do App
st.set_page_config(page_title="Central de Futebol Global", page_icon="⚽", layout="wide")

st.title("⚽ Central de Inteligência - Futebol Global")
st.markdown("Painel profissional de análise de desempenho, estatísticas e métricas das principais ligas do mundo.")

# Barra lateral para seleção global de ligas
st.sidebar.header("Filtros Globais")
liga_escolhida = st.sidebar.selectbox(
    "Selecione a Liga Principal:",
    [
        "Brasileirão (Brasil)", 
        "Premier League (Inglaterra)", 
        "La Liga (Espanha)", 
        "Bundesliga (Alemanha)", 
        "Serie A (Itália)",
        "Ligue 1 (França)",
        "Primeira Liga (Portugal)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("🟢 **Estado do Motor:** Ativo e Otimizado.")

# Base de Dados Global estruturada de Alta Precisão
def obter_dados_liga(liga):
    if "Brasileirão" in liga:
        return pd.DataFrame({
            'Equipa': ['Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Bahia', 'Cruzeiro'],
            'Jogos': [38, 38, 38, 38, 38, 38, 38, 38],
            'Pontos': [79, 73, 68, 65, 65, 59, 53, 51],
            'Golos Marcados': [56, 64, 58, 55, 52, 50, 48, 44],
            'Golos Sofridos': [28, 31, 35, 38, 33, 40, 42, 45]
        })
    elif "Premier League" in liga:
        return pd.DataFrame({
            'Equipa': ['Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham', 'Chelsea', 'Newcastle'],
            'Jogos': [38, 38, 38, 38, 38, 38, 38],
            'Pontos': [91, 89, 82, 68, 66, 63, 60],
            'Golos Marcados': [96, 91, 86, 76, 74, 77, 85],
            'Golos Sofridos': [34, 29, 41, 61, 61, 63, 62]
        })
    elif "La Liga" in liga:
        return pd.DataFrame({
            'Equipa': ['Real Madrid', 'Barcelona', 'Girona', 'Atlético de Madrid', 'Athletic Bilbao', 'Real Sociedad'],
            'Jogos': [38, 38, 38, 38, 38, 38],
            'Pontos': [95, 85, 81, 76, 68, 60],
            'Golos Marcados': [87, 79, 85, 70, 61, 51],
            'Golos Sofridos': [26, 44, 46, 43, 37, 39]
        })
    elif "Bundesliga" in liga:
        return pd.DataFrame({
            'Equipa': ['Bayer Leverkusen', 'Bayern de Munique', 'Stuttgart', 'Leipzig', 'Borussia Dortmund', 'Eintracht Frankfurt'],
            'Jogos': [34, 34, 34, 34, 34, 34],
            'Pontos': [90, 72, 73, 65, 63, 47],
            'Golos Marcados': [89, 94, 78, 77, 68, 51],
            'Golos Sofridos': [24, 45, 39, 39, 43, 50]
        })
    elif "Serie A" in liga:
        return pd.DataFrame({
            'Equipa': ['Inter de Milão', 'AC Milan', 'Juventus', 'Atalanta', 'Bologna', 'Roma'],
            'Jogos': [38, 38, 38, 38, 38, 38],
            'Pontos': [94, 75, 71, 69, 68, 63],
            'Golos Marcados': [89, 76, 54, 72, 54, 65],
            'Golos Sofridos': [22, 43, 31, 42, 32, 46]
        })
    elif "Ligue 1" in liga:
        return pd.DataFrame({
            'Equipa': ['Paris Saint-Germain', 'Monaco', 'Brest', 'Lille', 'Nice', 'Lens'],
            'Jogos': [34, 34, 34, 34, 34, 34],
            'Pontos': [76, 67, 61, 59, 55, 51],
            'Golos Marcados': [81, 68, 53, 52, 40, 45],
            'Golos Sofridos': [33, 42, 34, 34, 29, 37]
        })
    else:
        return pd.DataFrame({
            'Equipa': ['Sporting CP', 'Benfica', 'FC Porto', 'Braga', 'Vitória SC', 'Moreirense'],
            'Jogos': [34, 34, 34, 34, 34, 34],
            'Pontos': [90, 80, 72, 68, 63, 49],
            'Golos Marcados': [96, 77, 63, 71, 52, 36],
            'Golos Sofridos': [20, 28, 27, 50, 38, 35]
        })

df_app = obter_dados_liga(liga_escolhida)

# Processamento de Métricas Avançadas Automáticas
df_app['Saldo de Golos'] = df_app['Golos Marcados'] - df_app['Golos Sofridos']
df_app['Média Marcados'] = (df_app['Golos Marcados'] / df_app['Jogos']).round(2)
df_app['Aproveitamento (%)'] = ((df_app['Pontos'] / (df_app['Jogos'] * 3)) * 100).round(1)
df_app = df_app.sort_values(by='Pontos', ascending=False).reset_index(drop=True)

# Área Principal do App
st.subheader(f"📊 Painel Analítico: {liga_escolhida}")

# Cards de Destaque
col1, col2, col3, col4 = st.columns(4)
col1.metric("Líder Atual", df_app.iloc[0]['Equipa'])
col2.metric("Pontuação", f"{df_app.iloc[0]['Pontos']} pts")
col3.metric("Aproveitamento", f"{df_app.iloc[0]['Aproveitamento (%)']}%")
col4.metric("Média Golos/Jogo", df_app.iloc[0]['Média Marcados'])

# Tabela Interativa
st.markdown("### 📋 Tabela de Classificação & Métricas")
st.dataframe(df_app, use_container_width=True)

# Gráfico interativo
st.markdown("### 📈 Comparativo de Pontuação")
st.bar_chart(df_app.set_index('Equipa')['Pontos'])
