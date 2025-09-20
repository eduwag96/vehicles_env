import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Separamos model en seccion fabricante/modelo
car_data[['manufacturer','model']] = car_data['model'].str.split(' ', n=1, expand=True)

# Anadimos tabla con informacion general de los datos
st.header('Data viewer')

# Crear checkbox para data viewer
df_button = st.toggle('Build data')

if df_button:
   # Mensaje de activacion
   st.write('Data activated!')

   st.dataframe(car_data)

# Encabezado histograma 1
st.header('Vehicle types by manufacturer')

# Crear un checkbox en la aplicacion Streamlit

hist_button_1 = st.toggle('Build hist 1')

# Boton para generar histograma
if hist_button_1:
    # Mensaje de activacion
    st.write('Hist activated!')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = px.histogram(car_data, x='manufacturer', color='type')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar el gráfico Plotly
    fig.show()

# Encabezado histograma 2
st.header('Histogram of condition vs model_year')

# Crear un checkbox en la aplicacion Streamlit

hist_button_2 = st.toggle('Build hist 2')

# Boton para generar histograma
if hist_button_2:
    # Mensaje de activacion
    st.write('Hist activated!')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = px.histogram(car_data, x='model_year', color='condition')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar el gráfico Plotly
    fig.show()

# Encabezado histograma 3
st.header('Compare price distribution between manufacturers')

# Anadimos select box para comparacion por desicion del usuario
option_1 = st.selectbox('Select data 1 (x)', car_data.columns, placeholder='Select data')
option_2 = st.selectbox('Select data 2 (y)', car_data.columns, placeholder='Select data')

# Crear un checkbox en la aplicacion Streamlit

hist_button_3 = st.toggle('Build scatter')

# Boton para generar histograma
if hist_button_3:
    # Mensaje de activacion
    st.write('Scatter activated!')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = px.scatter(car_data, x=option_1, y=option_2, color='manufacturer')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar el gráfico Plotly
    fig.show()