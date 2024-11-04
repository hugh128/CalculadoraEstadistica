import flet as ft
import subprocess
import os

def main(page: ft.Page):
    page.title = "Ventana Principal"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Estilo de la página
    page.bgcolor = "#F5F5F5"  # Color de fondo suave
    page.padding = 20

    # Título
    title = ft.Text("Aplicaciones de Gráficas y Tablas", size=30, weight=ft.FontWeight.BOLD, color="#4A4A4A")
    
    # Ruta base del directorio actual
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Funciones para ejecutar cada archivo
    def abrir_frecuencias(e):
        subprocess.Popen(["python", os.path.join(base_dir, "FrecuenciasFlet.py")])

    def abrir_grafica_barras(e):
        subprocess.Popen(["python", os.path.join(base_dir, "grafica_barras.py")])

    def abrir_grafica_pastel(e):
        subprocess.Popen(["python", os.path.join(base_dir, "grafica_pastel.py")])

    def abrir_grafica_tiempo(e):
        subprocess.Popen(["python", os.path.join(base_dir, "GraficaTiempoFlet.py")])

    def abrir_tabla_frecuencia(e):
        subprocess.Popen(["python", os.path.join(base_dir, "tabla_frecuencia.py")])

    # Crear botones para cada archivo
    btn_frecuencias = ft.ElevatedButton("Frecuencias", on_click=abrir_frecuencias, bgcolor="#6200EE", color="white")
    btn_grafica_barras = ft.ElevatedButton("Gráfica Barras", on_click=abrir_grafica_barras, bgcolor="#6200EE", color="white")
    btn_grafica_pastel = ft.ElevatedButton("Gráfica Pastel", on_click=abrir_grafica_pastel, bgcolor="#6200EE", color="white")
    btn_grafica_tiempo = ft.ElevatedButton("Gráfica Tiempo", on_click=abrir_grafica_tiempo, bgcolor="#6200EE", color="white")
    btn_tabla_frecuencia = ft.ElevatedButton("Tabla Frecuencia", on_click=abrir_tabla_frecuencia, bgcolor="#6200EE", color="white")

    # Crear una fila para los botones
    button_row = ft.Row(
        controls=[
            btn_frecuencias,
            btn_grafica_barras,
            btn_grafica_pastel,
            btn_grafica_tiempo,
            btn_tabla_frecuencia,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10  # Espaciado entre botones
    )

    # Añadir el título y los botones a la página
    page.add(title, ft.Divider(), button_row)

# Ejecutar la aplicación
ft.app(target=main)

