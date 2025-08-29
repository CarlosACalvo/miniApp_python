import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🌸 Análisis interactivo del dataset Iris")

# Cargar dataset desde scikit-learn (se baja automáticamente)
from sklearn.datasets import load_iris
iris = load_iris(as_frame=True)
df = iris.frame

st.write("Vista previa de los datos:")
st.dataframe(df.head())

# Filtros
st.sidebar.header("Filtros")
columna = st.sidebar.selectbox("Selecciona una variable numérica", df.columns[:-1])
especie = st.sidebar.multiselect("Selecciona especie", df["target"].unique(), default=df["target"].unique())

df_filtrado = df[df["target"].isin(especie)]

# Gráfico
st.subheader(f"Distribución de {columna}")
fig, ax = plt.subplots()
sns.histplot(df_filtrado, x=columna, hue="target", kde=True, ax=ax)
st.pyplot(fig)

# Estadísticas
st.subheader("Estadísticas descriptivas")
st.write(df_filtrado.groupby("target")[columna].describe())
