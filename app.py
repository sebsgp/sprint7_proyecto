import pandas as pd
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv(
    "/Users/Sebastian/VScode/Proyecto_sprint7/sprint7_proyecto/vehicles_us.csv")

st.header("Análisis de anuncios de venta de coches")

build_histogram = st.checkbox("Construir histograma")
build_scatter = st.checkbox("Construir gráfico de dispersión")

if build_histogram:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title_text="Distribución del Odómetro")

    st.plotly_chart(fig, width="stretch")

if build_scatter:
    st.write("Creación de un gráfico de dispersión: precio vs. odómetro")

    fig = go.Figure(
        data=[go.Scatter(x=car_data["odometer"],
                         y=car_data["price"], mode="markers")]
    )
    fig.update_layout(
        title_text="Precio vs. Odómetro",
        xaxis_title="Odómetro (millas)",
        yaxis_title="Precio (USD)",
    )

    st.plotly_chart(fig, width="stretch")
