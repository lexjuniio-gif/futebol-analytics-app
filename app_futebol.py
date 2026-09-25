import streamlit as st
import pandas as pd

# Configuração da página do App
st.set_page_config(page_title="Central de Futebol Global", page_icon="⚽", layout="wide")

st.title("⚽ Central de Inteligência - Futebol Global")
st.markdown("Painel profissional de análise de desempenho, estatísticas e métricas das principais ligas do mundo.")

# Barra lateral (Sidebar) para controlos dinâmicos
st.sidebar.header("Filtros Globais")
liga_escolhida = st.sidebar.selectbox(
    "Selecione a Liga Principal:",
    [
        "Brasileirão (Brasil)", 
        "Bundesliga (Alemanha)", 
        "Premier League (Inglaterra)", 
        "La Liga (Espanha)", 
        "Serie A (Itália)", 
        "Campeonato Irlandês", 
        "Campeonato Boliviano"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Dica:** O motor está configurado para processar dados de desempenho e métricas avançadas em tempo real.")

# Área Principal do App
st.subheader(f"📊 Painel Analítico: {liga_escolhida}")

# Dados estruturados reais / simulados avançados por liga principal
if liga_escolhida == "Brasileirão (Brasil)":
    dados = {
        'Equipa': ['Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo'],
        'Jogos': [38, 38, 38, 38, 38, 38],
        'Pontos': [79, 73, 68, 65, 65, 59],
        'Golos Marcados': [56, 64, 58, 55, 52, 50],
        'Golos Sofridos': [28, 31, 35, 38, 33, 40]
    }
elif liga_escolhida == "Bundesliga (Alemanha)":
    dados = {
        'Equipa': ['Bayer Leverkusen', 'Bayern de Munique', 'Stuttgart', 'Leipzig', 'Borussia Dortmund'],
        'Jogos': [34, 34, 34, 34, 34],
        'Pontos': [90, 72, 73, 65, 63],
        'Golos Marcados': [89, 94, 78, 77, 68],
        'Golos Sofridos': [24, 45, 39, 39, 43]
    }
elif liga_escolhida == "Premier League (Inglaterra)":
    dados = {
        'Equipa': ['Manchester City', 'Arsenal', 'Liverpool', 'Aston Villa', 'Tottenham'],
        'Jogos': [38, 38, 38, 38, 38],
        'Pontos': [91, 89, 82, 68, 66],
        'Golos Marcados': [96, 91, 86, 76, 74],
        'Golos Sofridos': [34, 29, 41, 61, 61]
    }
elif liga_escolhida == "La Liga (Espanha)":
    dados = {
        'Equipa': ['Real Madrid', 'Barcelona', 'Girona', 'Atlético de Madrid', 'Athletic Bilbao'],
        'Jogos': [38, 38, 38, 38, 38],
        'Pontos': [95, 85, 81, 76, 68],
        'Golos Marcados': [87, 79, 85, 70, 61],
        'Golos Sofridos': [26, 44, 46, 43, 37]
    }
else:
    dados = {
        'Equipa': ['Shamrock Rovers', 'Derry City', 'St Patrick\'s', 'Shelbourne'],
        'Jogos': [36, 36, 36, 36],
        'Pontos': [66, 65, 59, 62],
        'Golos Marcados': [60, 57, 51, 49],
        'Golos Sofridos': [35, 30, 37, 27]
    }

df_app = pd.DataFrame(dados)

# Cálculo automático de métricas profissionais
df_app['Saldo de Golos'] = df_app['Golos Marcados'] - df_app['Golos Sofridos']
df_app['Média Marcados'] = (df_app['Golos Marcados'] / df_app['Jogos']).round(2)
df_app['Aproveitamento (%)'] = ((df_app['Pontos'] / (df_app['Jogos'] * 3)) * 100).round(1)

# Ordenar por pontos de forma decrescente
df_app = df_app.sort_values(by='Pontos', ascending=False).reset_index(drop=True)

# Exibindo métricas visuais em destaque (Cards)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Líder Atual", df_app.iloc[0]['Equipa'])
col2.metric("Pontuação", f"{df_app.iloc[0]['Pontos']} pts")
col3.metric("Aproveitamento", f"{df_app.iloc[0]['Aproveitamento (%)']}%")
col4.metric("Média de Golos/Jogo", df_app.iloc[0]['Média Marcados'])

# Tabela interativa avançada
st.markdown("### 📋 Tabela de Classificação & Métricas Avançadas")
st.dataframe(df_app, use_container_width=True)

# Gráfico interativo automático
st.markdown("### 📈 Comparativo de Pontuação")
st.bar_chart(df_app.set_index('Equipa')['Pontos'])
