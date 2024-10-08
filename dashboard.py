import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")


df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2) 
col3, col4, col5 = st.columns(3) 


# Criando os gráficos
#Grafico 1
grafico_um = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento mensal")
col1.plotly_chart(grafico_um, use_container_width=True)

#Grafico 2
grafico_dois = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(grafico_dois, use_container_width=True)

#Grafico 3
total_por_cidade = df_filtered.groupby("City")[["Total"]].sum().reset_index()
grafico_tres = px.bar(total_por_cidade, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(grafico_tres, use_container_width=True)

#Grafico 4
grafico_quatro = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento tipo de pagamento")
col4.plotly_chart(grafico_quatro, use_container_width=True)

#Grafico 5
media_avaliacao = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
grafico_cinco = px.bar(df_filtered, x="City", y="Rating", title="Avaliação")
col5.plotly_chart(grafico_cinco, use_container_width=True)

