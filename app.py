# importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
import streamlit as strm

# Cabeçalho
strm.header('Visualização do conjunto de dados de anúncios de vendas de carros graficamente')

# lendo os dados
df_cars = pd.read_csv('vehicles_us.csv') 

# criar um botão
hist_button = strm.button('Criar um histograma')
scatter_button = strm.button('Criar gráfico de dispersão')
box_button = strm.button('Criar um boxplot')
bar_button = strm.button('Criar um gráfico de barras')

# se o botão for clicado
if hist_button:
  # escrever uma mensagem
  strm.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
  # criar um histograma
  fig1 = px.histogram(df_cars, x='odometer')
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig1, use_container_width=True)

if scatter_button:
  # escrever uma mensagem
  strm.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
  # criar um histograma
  fig2 = px.scatter(df_cars, x='model_year', y='odometer')
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig2, use_container_width=True)

if box_button:
  # escrever uma mensagem
  strm.write('Criando um boxplot para o conjunto de dados de anúncios de vendas de carros')
  # criar um histograma
  fig2 = px.box(df_cars, x='cylinders')
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig2, use_container_width=True)

if bar_button:
  # escrever uma mensagem
  strm.write('Criando um gráfico de barras para o conjunto de dados de anúncios de vendas de carros')
  # criar um histograma
  fig2 = px.bar(df_cars, x='paint_color')
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig2, use_container_width=True)

# criar uma caixa de seleção
build_histogram = strm.checkbox('Criar um histograma')
build_scatter = strm.checkbox('Criar um gráfico de dispersão')
build_box = strm.checkbox('Criar um boxplot')
build_bar = strm.checkbox('Criar um gráfico de barras')

# se a caixa de seleção for selecionada
if build_histogram: 
  strm.write('Criando um histograma para a coluna odometer')

if build_scatter: 
  strm.write('Criando um gráfico de dispersão para as colunas model_year e odometer')

if build_box: 
  strm.write('Criando um boxplot para a coluna cylinders')

if build_bar: 
  strm.write('Criando um gráfico de barras para a coluna paint_color')
