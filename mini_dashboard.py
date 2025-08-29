import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la app
st.title("Dashboard de Ventas 📊")

# Cargar datos
df = pd.read_csv("ventas.csv")

# Mostrar una muestra de los datos
st.write("Vista previa de los datos:", df.head())

# Filtros
region = st.selectbox("Selecciona región", df["region"].unique())
df_filtrado = df[df["region"] == region]

# KPI simple
total_ventas = (df_filtrado["cantidad"] * df_filtrado["precio"]).sum()
st.metric("Ventas totales", f"${total_ventas:,.0f}")

# Gráfico de ventas por producto
ventas_por_producto = df_filtrado.groupby("producto")["cantidad"].sum()

fig, ax = plt.subplots()
ventas_por_producto.plot(kind="bar", ax=ax)
plt.title("Ventas por producto")
st.pyplot(fig)