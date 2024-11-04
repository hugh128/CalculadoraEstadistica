import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt
import numpy as np

def main(page: ft.Page):
    page.title = "Tabla de Frecuencias con Histograma y Polígono de Frecuencia"

    # Inputs para ingresar los datos
    datos_input = ft.TextField(label="Datos (separados por comas)", width=400)
    intervalos_input = ft.TextField(label="Número de intervalos", width=200)
    
    # Botón para calcular la tabla de frecuencias
    calcular_button = ft.ElevatedButton("Calcular", on_click=lambda e: calcular_frecuencias())
    
    # Contenedores para la tabla de frecuencias y gráficos
    tabla_resultado = ft.Column()
    grafico_histograma = ft.Container(width=500, height=400)
    grafico_polinomio = ft.Container(width=500, height=400)
    
    # Función para calcular la tabla de frecuencias
    def calcular_frecuencias():
        try:
            # Leer datos ingresados
            datos = [float(d) for d in datos_input.value.split(",")]
            num_intervalos = int(intervalos_input.value)
            
            # Calcular intervalos y frecuencias
            min_dato, max_dato = min(datos), max(datos)
            rango = (max_dato - min_dato) / num_intervalos
            intervalos = [(min_dato + i * rango, min_dato + (i + 1) * rango) for i in range(num_intervalos)]
            
            # Inicializar variables para frecuencias y límites
            frecuencias = []
            marca_clase = []
            
            for limite_inf, limite_sup in intervalos:
                frecuencia = sum(1 for d in datos if limite_inf <= d < limite_sup)
                frecuencias.append(frecuencia)
                marca_clase.append((limite_inf + limite_sup) / 2)
            
            # Crear tabla de frecuencias
            tabla_resultado.controls.clear()
            tabla_resultado.controls.append(ft.Text("Tabla de Frecuencias", weight="bold", size=18))
            tabla_resultado.controls.append(ft.Text("Límite Inferior | Límite Superior | Marca de Clase | Frecuencia"))

            for i in range(num_intervalos):
                tabla_resultado.controls.append(ft.Text(f"{intervalos[i][0]:.2f} - {intervalos[i][1]:.2f} | {marca_clase[i]:.2f} | {frecuencias[i]}"))

            # Graficar el histograma y el polígono de frecuencias
            graficar_histograma(marca_clase, frecuencias, rango)
            graficar_poligono(marca_clase, frecuencias)

            page.update()

        except ValueError:
            tabla_resultado.controls.clear()
            tabla_resultado.controls.append(ft.Text("Error: Asegúrate de ingresar datos válidos.", color="red"))
            page.update()
    
    # Función para graficar el histograma
    def graficar_histograma(marcas, frecuencias, ancho_intervalo):
        fig, ax = plt.subplots()
        ax.bar(marcas, frecuencias, width=ancho_intervalo * 0.9, color="skyblue", edgecolor="black")
        ax.set_xlabel("Marca de Clase")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Histograma de Frecuencias")
        ax.grid(True, linestyle="--", alpha=0.7)

        grafico_histograma.content = MatplotlibChart(fig)

    # Función para graficar el polígono de frecuencias
    def graficar_poligono(marcas, frecuencias):
        fig, ax = plt.subplots()
        ax.plot(marcas, frecuencias, marker="o", color="royalblue", linestyle="-", linewidth=2, markersize=6)
        ax.set_xlabel("Marca de Clase")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Polígono de Frecuencias")
        ax.grid(True, linestyle="--", alpha=0.7)

        grafico_polinomio.content = MatplotlibChart(fig)

    # Agregar componentes a la página
    page.add(
        ft.Row([datos_input, intervalos_input, calcular_button]),
        tabla_resultado,
        ft.Row([grafico_histograma, grafico_polinomio])
    )

ft.app(target=main)
