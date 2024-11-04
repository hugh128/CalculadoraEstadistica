import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt

# Estilo de Matplotlib para gráficos modernos
plt.style.use('seaborn-v0_8-dark')  # Cambia el estilo a uno oscuro

# Función para crear la gráfica personalizada
def crear_grafica(valores_x, valores_y):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Personalización del gráfico de líneas
    ax.plot(valores_x, valores_y, marker="o", color="#4FADFF", linewidth=3, markersize=10, linestyle="-", label="Datos")
    ax.fill_between(valores_x, valores_y, color="#4FADFF", alpha=0.2)  # Fondo bajo la curva
    
    # Títulos y etiquetas personalizadas
    ax.set_xlabel("Valores X", fontsize=14, color="white")
    ax.set_ylabel("Valores Y", fontsize=14, color="white")
    ax.set_title("Gráfica de Serie de Tiempo", fontsize=18, color="white", pad=20)

    # Estilo de ejes
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("gray")
    ax.spines["bottom"].set_color("gray")
    ax.tick_params(colors="lightgray")

    # Fondo del gráfico y de los ejes
    ax.set_facecolor("#2B2B2B")
    fig.patch.set_facecolor("#222222")

    # Leyenda y grilla personalizada
    ax.legend(loc="upper left", fontsize=12, facecolor="#333333", edgecolor="none", labelcolor="white")
    ax.grid(True, color="gray", linestyle=":", linewidth=0.5, alpha=0.5)

    return fig

# Función principal de Flet
def main(page: ft.Page):
    page.title = "Gráfica De Tiempo"
    page.bgcolor = "#222222"

    # Campos de entrada para valores X e Y
    valores_x = ft.TextField(label="Valores X (separados por comas)", width=300, bgcolor="#FFFFFF", color="white")
    valores_y = ft.TextField(label="Valores Y (separados por comas)", width=300, bgcolor="#FFFFFF", color="white")

    # Contenedor para mostrar la gráfica
    contenedor_grafica = ft.Container(width=800, height=500, bgcolor="#333333", border_radius=10, padding=10)

    # Función para manejar el evento de clic en el botón "Graficar"
    def graficar_click(e):
        x = [float(i) for i in valores_x.value.split(",")]
        y = [float(i) for i in valores_y.value.split(",")]
        fig = crear_grafica(x, y)
        contenedor_grafica.content = MatplotlibChart(fig)
        page.update()

    # Botón para generar la gráfica
    boton_graficar = ft.ElevatedButton(text="Generar Gráfica", on_click=graficar_click, bgcolor="#4FADFF", color="white")

    # Añadir elementos a la página
    page.add(ft.Column([valores_x, valores_y, boton_graficar, contenedor_grafica], alignment="center", spacing=10))

# Ejecutar la aplicación
ft.app(target=main)
