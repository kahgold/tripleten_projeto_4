import pandas as pd
import plotly.express as px
import streamlit as stm

st.header('Demosntrando o conjunto de dados de anúncios de vendas de carros graficamente.')

# lendo os dados
df_cars = pd.read_csv('vehicles_us.csv')


# criar um botão
hist_button = stm.button('Criar histograma') 
scat_button = stm.button('Criar gráfico de dispersão') 
box_buttom = stm.button('Criar boxplot')
bar_button = stm.buttom('Criar gráfico de barra')


# se o botão for clicado
if hist_button: 
     # escrever uma mensagem
     stm.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
     # criar um histograma
     fig1 = px.histogram(df_cars, x="odometer")
     # exibir um gráfico Plotly interativo
     stm.plotly_chart(fig1, use_container_width=True)

if scat_button: 
     # escrever uma mensagem
     stm.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
     # criar um gráfico de dispersão
     fig2 = px.scatter(df_cars, x='model_year', y='odometer')
     # exibir um gráfico Plotly interativo
     stm.plotly_chart(fig2, use_container_width=True)

if box_button:
     # escrever uma mensagem
     stm.write('Criando uma matriz de correlação para o conjunto de dados de anúncios de vendas de carros')
     # criar um boxplot
     fig4 = px.box(df_cars, x='paint_color', y='price', color='paint_color')
     # exibir um gráfico Plotly interativo
     stm.plotly_chart(fig4, use_container_width=True)

if bar_button:
     # escrever uma mensagem
     stm.write('Criando uma matriz de correlação para o conjunto de dados de anúncios de vendas de carros')
     # criar um gráfico de barra
     fig5 = px.box(df_cars, x="paint_color", template='none', color='paint_color')
     # exibir um gráfico Plotly interativo
     stm.plotly_chart(fig5, use_container_width=True)


# criar uma caixa de seleção
build_histogram = stm.checkbox('Criar um histograma')
build_scatter = stm.checkbox('Criar um gráfico de dispersão')
build_box = stm.checkbox('Criar um boxplot')
build_bar = stm.checkbox('Criar um boxplot')


# se a caixa de seleção for selecionada
if build_histogram: 
     stm.write('Criando um histograma para a coluna odometer')

# se a caixa de seleção for selecionada
if build_scatter: 
     stm.write('Criando um gráfico de dispersão para as colunas model_year e odometer')

# se a caixa de seleção for selecionada
if build_box:
     stm.write('Criando um boxplot para as colunas paint_color e price')

# se a caixa de seleção for selecionada
if build_bar:
     stm.write('Criando um gráfico de barra para a coluna price')
