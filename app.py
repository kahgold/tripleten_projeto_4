import pandas as pd
import plotly.express as px
import streamlit as stm
     
df_cars = pd.read_csv('vehicles_us.csv') # lendo os dados
hist_button = stm.button('Criar histograma') # criar um botão
scat_button = stm.button('Criar gráfico de dispersão')
mtx_corr_button = tsm.button('Criar matriz de correlação')
     
if hist_button: # se o botão for clicado
     # escrever uma mensagem
     stm.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

if scat_button: # se o botão for clicado
     stm.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

if mtx_corr_button: # se o botão for clicado
     stm.write('Criando uma matriz de correlação para o conjunto de dados de anúncios de vendas de carros')

if box_button: # se o botão for clicado
     stm.write('Criando uma matriz de correlação para o conjunto de dados de anúncios de vendas de carros')
         
     # criar um histograma
     fig1 = px.histogram(df_cars, x="odometer")

     # criar um gráfico de dispersão
     fig2 = px.scatter(df_cars, x='model_year', y='odometer', color_discrete_sequence=px.colors.qualitative.Set3)

     # criar uma matriz de correlação
     fig3 = px.imshow(df_cars, df_cars.iloc[:, [0, 1, 4, 6, 10]].corr())

     # criar uma matriz de correlação
     fig4 = px.box(df_cars, x='paint_color', y='price', color='paint_color')
         
     # exibir um gráfico Plotly interativo
     stm.plotly_chart(fig1, use_container_width=True)
     stm.plotly_chart(fig2, use_container_width=True)
     stm.plotly_chart(fig3, use_container_width=True)
     stm.plotly_chart(fig4, use_container_width=True)

# criar uma caixa de seleção
build_histogram = stm.checkbox('Criar um histograma')
build_scatter = stm.checkbox('Criar um gráfico de dispersão)
build_mtx_corr = stm.checkbox('Criar uma matriz de correlação')
build_box = stm.checkbox('Criar um boxplot')

if build_histogram: # se a caixa de seleção for selecionada
     stm.write('Criando um histograma para a coluna odometer')

if build_scatter: # se a caixa de seleção for selecionada
    stm.write('Criando um gráfico de dispersão para as colunas model_year e odometer')

if build_mtx_corr: # se a caixa de seleção for selecionada
    stm.write('Criando uma matriz de correlação para o dataframe df_cars')

if 
