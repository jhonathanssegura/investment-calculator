import streamlit as st
import matplotlib.pyplot as plt

# Título
st.title("📈 Calculadora de Inversiones")

# Entrada de datos
monto_inicial = st.number_input("💰 Monto inicial ($)", min_value=0.0, value=1000.0)
tasa = st.number_input("📊 Tasa de retorno (%)", min_value=0.0, value=10.0)
periodo = st.selectbox("⏳ ¿Plazo en años o meses?", ["Años", "Meses"])
duracion = st.number_input(f"📆 Número de {periodo.lower()}", min_value=1, value=12)

# Cálculo de interés compuesto
def calcular_inversion(monto, tasa, tiempo, es_anual=True):
    resultados = []
    for t in range(1, tiempo + 1):
        if es_anual:
            valor = monto * ((1 + tasa / 100) ** t)
        else:
            valor = monto * ((1 + tasa / 100) ** t)
        resultados.append(valor)
    return resultados

# Determinar si es anual o mensual
es_anual = periodo == "Años"
tiempo_total = duracion

# Cálculo
valores = calcular_inversion(monto_inicial, tasa, tiempo_total, es_anual)
valor_final = valores[-1]

# Mostrar resultados
st.success(f"📌 Valor final estimado: ${valor_final:,.2f}")

# Gráfico
fig, ax = plt.subplots()
ax.plot(range(1, tiempo_total + 1), valores, marker='o', color='green')
ax.set_title("Crecimiento de la inversión")
ax.set_xlabel("Tiempo ({}s)".format("año" if es_anual else "mes"))
ax.set_ylabel("Monto ($)")
ax.grid(True)

# Mostrar gráfico
st.pyplot(fig)
