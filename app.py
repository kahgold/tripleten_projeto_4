# importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
import streamlit as strm

# Cabeçalho
strm.header('Visualização do conjunto de dados de anúncios de vendas de carros graficamente')

# lendo os dados
df_cars = pd.read_csv('vehicles_us.csv') 

# criar um botão
hist_button = strm.button('Criar histograma')
scatter_button = strm.button('Criar gráfico de dispersão')
mtz_corr_button = strm.button('Criar matriz de correlação')
box_button = strm.button('Criar boxplot')
bar_button = strm.button('Criar gráfico de barras')

# criar uma caixa de seleção
# build_histogram = strm.checkbox('Criar um histograma')
# build_scatter = strm.checkbox('Criar um gráfico de dispersão')
# build_scatter = strm.checkbox('Criar uma matriz de correlação')
# build_box = strm.checkbox('Criar um boxplot')
# build_bar = strm.checkbox('Criar um gráfico de barras')

# se o botão for clicado
if hist_button:
  # criar uma caixa de seleção
  build_histogram = strm.checkbox('Criar um histograma')
  # escrever uma mensagem
  strm.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
  # criar um histograma
  fig1 = px.histogram(df_cars, x='odometer', template='none', nbins=20, text_auto=True,
                      color_discrete_sequence=px.colors.qualitative.Antique)
   # Atualizando o layout, se necessário
  fig1.update_layout(title='Visualização da coluna - ODOMETER', autosize=False, width=500, height=500)
  fig1.update_traces(marker_line_width=1, marker_line_color="black")
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig1, use_container_width=True)

if scatter_button:
  # criar uma caixa de seleção
  build_scatter = strm.checkbox('Criar um gráfico de dispersão')
  # escrever uma mensagem
  strm.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
  # criar um gráfico de dispersão
  fig2 = px.scatter(df_cars, x='model_year', y='odometer', 
                    color_discrete_sequence=px.colors.qualitative.Set3) 

  fig2.update_traces(marker=dict(size=8, line=dict(width=2, color='grey')), 
                  selector=dict(mode='markers'))

  fig2.update_layout(scattermode="group", scattergap=0.75, 
                     title='Gráfico de Dispersão entre model_year e odometer', 
                     autosize=False, width=500, height=500)
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig2, use_container_width=True)
  # se a caixa de seleção for selecionada
  
if mtz_corr_button:
  # criar uma caixa de seleção
  build_scatter = strm.checkbox('Criar uma matriz de correlação')
  # escrever uma mensagem
  strm.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
  # criar uma matriz de correlação
  corr_mtz = df_cars.iloc[:, [0, 1, 4, 6, 10]].corr()
  fig3 = px.imshow(df_cars, corr_mtz, text_auto=True,
                   color_continuous_scale=[(0, "blue"), (0.5, "orange"), (1, "purple")])
  fig3.update_layout(title='Matriz de Correlação', autosize=False, width=500, height=500)
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig3, use_container_width=True)

if box_button:
  # criar uma caixa de seleção
  build_box = strm.checkbox('Criar um boxplot')
  # escrever uma mensagem
  strm.write('Criando um boxplot para o conjunto de dados de anúncios de vendas de carros')
  # criar um boxplot
  fig4 = px.box(df_cars, x='cylinders', color_discrete_sequence=px.colors.qualitative.Dark24_r)
  fig4.update_layout(title='Boxplot da Coluna "cylinders"', autosize=False, width=500, height=500)
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig4, use_container_width=True)

if bar_button:
  # criar uma caixa de seleção
  build_bar = strm.checkbox('Criar um gráfico de barras')
  # escrever uma mensagem
  strm.write('Criando um gráfico de barras para o conjunto de dados de anúncios de vendas de carros')
  # criar um gráfico de barras
  fig5 = px.bar(df_cars, x='paint_color', template='none', color='paint_color')
  fig5.update_layout(title='Contagem de Veículos por Cor', autosize=False, width=500, height=500
  # exibir um gráfico Plotly interativo
  strm.plotly_chart(fig5, use_container_width=True)
