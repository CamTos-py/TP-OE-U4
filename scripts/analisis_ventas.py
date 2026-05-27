
# ==============================================================
# Script de Análisis de Ventas
# Autor: Camila Tosti (Rol: Paco - P2)
# Descripción: Analiza el dataset de ventas usando solo
# estructuras básicas de Python (listas, diccionarios, csv).
# ==============================================================

import csv
import matplotlib.pyplot as plt

# --- CARGA DE DATOS ---

ventas = []
with open("datos/ventas.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        ventas.append({
            "producto": fila["producto"],
            "cantidad": int(fila["cantidad"]),
            "precio": int(fila["precio"]),
            "fecha": fila["fecha"]
        })

# --- INDICADOR 1: VENTAS TOTALES ---

total_ventas = 0
for venta in ventas:
    total_ventas = total_ventas + (venta["cantidad"] * venta["precio"])

print("Ventas totales: $" + str(total_ventas))

# --- INDICADOR 2: PRODUCTO MÁS VENDIDO ---

cantidades_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in cantidades_por_producto:
        cantidades_por_producto[producto] = cantidades_por_producto[producto] + venta["cantidad"]
    else:
        cantidades_por_producto[producto] = venta["cantidad"]

producto_mas_vendido = ""
mayor_cantidad = 0
for producto, cantidad in cantidades_por_producto.items():
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        producto_mas_vendido = producto

print("Producto más vendido: " + producto_mas_vendido + " (" + str(mayor_cantidad) + " unidades)")

# --- INDICADOR 3: VENTAS POR MES ---

ingresos_por_mes = {}
for venta in ventas:
    mes = venta["fecha"][:7]
    ingreso = venta["cantidad"] * venta["precio"]
    if mes in ingresos_por_mes:
        ingresos_por_mes[mes] = ingresos_por_mes[mes] + ingreso
    else:
        ingresos_por_mes[mes] = ingreso

print("\nVentas por mes:")
for mes, ingreso in ingresos_por_mes.items():
    print("  " + mes + ": $" + str(ingreso))

# --- GRÁFICO ---
meses = list(ingresos_por_mes.keys())
ingresos = list(ingresos_por_mes.values())

plt.figure(figsize=(8, 5))
plt.bar(meses, ingresos, color="steelblue")
plt.title("Evolución de Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ingreso ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("resultados/grafico_ventas.png")
plt.show()
print("\nGráfico guardado en resultados/grafico_ventas.png")
