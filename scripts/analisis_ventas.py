
# ==============================================================
# Script de Análisis de Ventas
# Autor: Camila Tosti (Rol: Paco - P2)
# Descripción: Analiza el dataset de ventas para calcular
# indicadores clave y generar visualizaciones.
# ==============================================================

import pandas as pd
import matplotlib.pyplot as plt

# --- CARGA DE DATOS ---
# Usamos ruta relativa para garantizar reproducibilidad en cualquier entorno
df = pd.read_csv("datos/ventas.csv")

# --- INDICADORES ---
# Calculamos el ingreso total por fila (precio x cantidad)
df["ingreso"] = df["cantidad"] * df["precio"]

# Ventas totales globales
total_ventas = df["ingreso"].sum()
print(f"Ventas totales: ${total_ventas:,.0f}")

# Producto más vendido (por cantidad)
mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print(f"Producto más vendido: {mas_vendido}")

# Ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["ingreso"].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

# --- GRÁFICO ---
# Graficamos la evolución de ventas mensuales para visualizar tendencias
ventas_por_mes.plot(kind="bar", color="steelblue", figsize=(8,5))
plt.title("Evolución de Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ingreso ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Guardamos el gráfico en /resultados
plt.savefig("resultados/grafico_ventas.png")
plt.show()
print("\nGráfico guardado en resultados/grafico_ventas.png")
