import streamlit as st
import pandas as pd

# URL del snapshot en GitHub
url = "https://raw.githubusercontent.com/OscarMC28/hr-snapshot-demo/main/latest_snapshot.csv"

st.title("Dashboard HR - Snapshot desde GitHub")

# Cargar datos
data = pd.read_csv(url)
st.write("Datos cargados desde GitHub:")
st.dataframe(data)

# Ejemplo gráfico simple
st.bar_chart(data["Position"].value_counts())
