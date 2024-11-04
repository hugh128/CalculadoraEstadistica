import flet as ft
import matplotlib.pyplot as plt
import io
import base64

def main(page: ft.Page):
    page.title = "Generador de Gráfica de Barras"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Mensaje de bienvenida
    mensaje_bienvenida = ft.Text("Ingrese los datos para el eje X y el eje Y, separados por comas")

    # Campos de entrada para los datos
    datos_x = ft.TextField(label="Datos para el eje X (separados por comas)", width=400)
    datos_y = ft.TextField(label="Datos para el eje Y (separados por comas)", width=400)

    # Área de mensaje para mostrar errores o información
    resultado_texto = ft.Text()

    # Imagen de la gráfica
    grafica_imagen = ft.Image(src="", width=500, height=400)  # Inicialmente vacía

    # Función para generar y mostrar la gráfica de barras
    def generar_grafica(e):
        datos_x_ingresados = datos_x.value
        datos_y_ingresados = datos_y.value

        try:
            # Convertir datos a listas
            etiquetas_x = datos_x_ingresados.split(",")
            valores_y = [float(num) for num in datos_y_ingresados.split(",")]

            # Verificar que ambas listas tengan la misma longitud
            if len(etiquetas_x) != len(valores_y):
                resultado_texto.value = "Error: La cantidad de datos en X y Y debe ser igual."
                page.update()
                return

            # Crear la gráfica de barras
            fig, ax = plt.subplots()
            ax.bar(etiquetas_x, valores_y)
            ax.set_xlabel("Eje X")
            ax.set_ylabel("Eje Y")
            ax.set_title("Gráfica de Barras")

            # Guardar la gráfica en memoria
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)

            # Convertir la imagen a base64 para mostrarla en Flet
            img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            grafica_imagen.src_base64 = img_base64
            buffer.close()

            # Limpiar el mensaje de error en caso de que haya funcionado correctamente
            resultado_texto.value = ""
            page.update()

        except ValueError:
            resultado_texto.value = "Error: Asegúrate de ingresar solo números para el eje Y."
            page.update()

    # Botón para generar la gráfica
    bntGenerar = ft.ElevatedButton("Generar Gráfica", on_click=generar_grafica)

    # Agregar componentes a la página
    page.add(mensaje_bienvenida, datos_x, datos_y, bntGenerar, resultado_texto, grafica_imagen)

# Ejecutar la aplicación
ft.app(target=main)

