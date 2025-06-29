import streamlit as st
import matplotlib.pyplot as plt

# Título
st.title("📈 Calculadora de Inversiones con Interés Compuesto")

# Entrada de datos
monto_inicial = st.number_input("💰 Monto inicial ($)", min_value=0.0, value=1000.0)
tasa = st.number_input("📊 Tasa de retorno (%)", min_value=0.0, value=10.0)
tipo_tasa = st.selectbox("📅 Tipo de tasa", ["Anual", "Mensual"])
periodo = st.selectbox("⏳ ¿Plazo en años o meses?", ["Años", "Meses"])
duracion = st.number_input(f"📆 Número de {periodo.lower()}", min_value=1, value=12)

# Convertir tasa y tiempo al mismo período
def convertir_tasa_y_periodo(tasa, tipo_tasa, periodo, duracion):
    if tipo_tasa == "Anual" and periodo == "Meses":
        tasa_convertida = tasa / 12
        tiempo_convertido = duracion
    elif tipo_tasa == "Mensual" and periodo == "Años":
        tasa_convertida = tasa
        tiempo_convertido = duracion * 12
    else:
        tasa_convertida = tasa
        tiempo_convertido = duracion
    return tasa_convertida, tiempo_convertido

# Cálculo de inversión
def calcular_inversion(monto, tasa_mensual, meses):
    resultados = []
    for t in range(1, meses + 1):
        valor = monto * ((1 + tasa_mensual / 100) ** t)
        resultados.append(valor)
    return resultados

# Procesamiento
tasa_mensual, tiempo_meses = convertir_tasa_y_periodo(tasa, tipo_tasa, periodo, duracion)
valores = calcular_inversion(monto_inicial, tasa_mensual, tiempo_meses)
ganancias = [valor - monto_inicial for valor in valores]
valor_final = valores[-1]

# Mostrar resultado
st.success(f"📌 Valor final estimado: ${valor_final:,.2f}")

# Gráfico con etiquetas de ganancia
fig, ax = plt.subplots()
x = list(range(1, tiempo_meses + 1))
ax.plot(x, valores, marker='o', color='green')
for i, (x_val, y_val, ganancia) in enumerate(zip(x, valores, ganancias)):
    ax.annotate(f"+${ganancia:,.2f}", (x_val, y_val), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

ax.set_title("Crecimiento de la inversión")
ax.set_xlabel("Tiempo (meses)")
ax.set_ylabel("Monto acumulado ($)")
ax.grid(True)

# Mostrar gráfico
st.pyplot(fig)
