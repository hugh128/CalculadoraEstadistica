import flet as ft
import matplotlib.pyplot as plt
import io
import base64

def main(page: ft.Page):
    page.title = "Generador de Gráfica de Pastel"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Mensaje de bienvenida
    mensaje_bienvenida = ft.Text("Ingrese las etiquetas y los datos para el gráfico de pastel, separados por comas")

    # Campos de entrada para las etiquetas y datos
    etiquetas_input = ft.TextField(label="Etiquetas (separadas por comas)", width=400)
    valores_input = ft.TextField(label="Valores (separados por comas)", width=400)

    # Área de mensaje para mostrar errores o información
    resultado_texto = ft.Text()

    # Imagen de la gráfica
    grafica_imagen = ft.Image(src="", width=500, height=400)

    # Función para generar y mostrar la gráfica de pastel
    def generar_grafica(e):
        etiquetas = etiquetas_input.value.split(",")
        valores = valores_input.value.split(",")

        try:
            # Convertir valores a números
            valores = [float(valor) for valor in valores]

            # Verificar que ambas listas tengan la misma longitud
            if len(etiquetas) != len(valores):
                resultado_texto.value = "Error: La cantidad de etiquetas y valores debe ser igual."
                page.update()
                return

            # Crear la gráfica de pastel
            fig, ax = plt.subplots()
            ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
            ax.axis("equal")  # Para hacer la gráfica circular

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
            resultado_texto.value = "Error: Asegúrate de ingresar solo números para los valores."
            page.update()

    # Botón para generar la gráfica
    bntGenerar = ft.ElevatedButton("Generar Gráfica de Pastel", on_click=generar_grafica)

    # Agregar componentes a la página
    page.add(mensaje_bienvenida, etiquetas_input, valores_input, bntGenerar, resultado_texto, grafica_imagen)

# Ejecutar la aplicación
ft.app(target=main)
