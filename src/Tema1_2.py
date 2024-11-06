import flet as ft
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter

# Tema 1: Tabla de Frecuencias
def tema1(page):
    # Lista para almacenar los números
    number_list = []

    # Etiqueta de instrucciones
    instruction_label = ft.Text("Ingresa números separados por comas y presiona 'Agregar'")

    # Campo de entrada de números
    number_input = ft.TextField(label="Números (separados por comas)", keyboard_type="text", width=300)

    # Área de resultados para mostrar los números ingresados o el resultado de ordenación
    result_area = ft.Text()

    # Tabla de frecuencias
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Número")),
            ft.DataColumn(ft.Text("Frecuencia")),
            ft.DataColumn(ft.Text("Frecuencia Relativa")),
            ft.DataColumn(ft.Text("Frecuencia Acumulada")),
        ],
        rows=[],
    )

    # Contenedor con scroll para la tabla usando ListView
    scrollable_table = ft.ListView(
        controls=[table],
        width=600,
        height=300,
        padding=10,
    )

    def add_number(e):
        try:
            numbers = [int(num.strip()) for num in number_input.value.split(",") if num.strip()]
            number_list.extend(numbers)
            number_input.value = ""
            result_area.value = "Números ingresados: " + ", ".join(map(str, number_list))
        except ValueError:
            result_area.value = "Por favor ingresa números válidos separados por comas."
        page.update()

    def sort_numbers(e):
        if number_list:
            number_list.sort()
            result_area.value = "Números ordenados: " + ", ".join(map(str, number_list))
        else:
            result_area.value = "No hay números para ordenar."
        page.update()

    def calculate_frequency(e):
        if number_list:
            table.rows.clear()
            number_counter = Counter(number_list)
            total_numbers = len(number_list)
            cumulative_frequency = 0.0

            for number, freq in number_counter.items():
                relative_frequency = freq / total_numbers
                cumulative_frequency += relative_frequency
                table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(number))),
                            ft.DataCell(ft.Text(str(freq))),
                            ft.DataCell(ft.Text(f"{relative_frequency:.4f}")),
                            ft.DataCell(ft.Text(f"{cumulative_frequency:.4f}")),
                        ]
                    )
                )

            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Total de datos:")),
                        ft.DataCell(ft.Text(str(total_numbers))),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                    ]
                )
            )
        else:
            result_area.value = "No hay números para calcular la frecuencia."
        page.update()

    def clear_numbers(e):
        number_list.clear()
        result_area.value = "Los números han sido limpiados."
        table.rows.clear()
        page.update()

    add_button = ft.ElevatedButton("Agregar números", on_click=add_number)
    sort_button = ft.ElevatedButton("Ordenar números", on_click=sort_numbers)
    frequency_button = ft.ElevatedButton("Calcular frecuencia", on_click=calculate_frequency)
    clear_button = ft.ElevatedButton("Limpiar números", on_click=clear_numbers)

    content = ft.Column(
        [
            instruction_label,
            number_input,
            ft.Row([add_button, sort_button, frequency_button, clear_button]),
            result_area,
            scrollable_table
        ],
        spacing=10,
    )
    
    return content

# Tema 2: Gráfica de Barras
def tema2(page):
    datos_x = ft.TextField(label="Datos X (separados por comas)", width=300)
    datos_y = ft.TextField(label="Datos Y (separados por comas)", width=300)
    resultado_texto = ft.Text()
    grafica_imagen = ft.Image(src="", width=500, height=400)

    def generar_grafica(e):
        try:
            etiquetas = datos_x.value.split(",")
            valores = list(map(float, datos_y.value.split(",")))
            if len(etiquetas) != len(valores):
                resultado_texto.value = "Error: La cantidad de datos en X y Y debe ser igual."
                return
            fig, ax = plt.subplots()
            ax.bar(etiquetas, valores)
            ax.set_xlabel("Eje X")
            ax.set_ylabel("Eje Y")
            ax.set_title("Gráfica de Barras")
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            grafica_imagen.src_base64 = img_base64
            resultado_texto.value = ""
            page.update()
        except ValueError:
            resultado_texto.value = "Error: Asegúrate de ingresar solo números para el eje Y."
            page.update()

    bntGenerar = ft.ElevatedButton("Generar Gráfica", on_click=generar_grafica)
    
    content = ft.Column(
        [
            datos_x,
            datos_y,
            bntGenerar,
            resultado_texto,
            grafica_imagen,
        ],
        spacing=10,
    )
    return content

# Tema 3: Gráfica de Pastel
def tema3(page):
    etiquetas_input = ft.TextField(label="Etiquetas (separadas por comas)", width=300)
    valores_input = ft.TextField(label="Valores (separados por comas)", width=300)
    resultado_texto = ft.Text()
    grafica_imagen = ft.Image(src="", width=500, height=400)

    def generar_grafica(e):
        etiquetas = etiquetas_input.value.split(",")
        valores = list(map(float, valores_input.value.split(",")))
        if len(etiquetas) != len(valores):
            resultado_texto.value = "Error: La cantidad de etiquetas y valores debe ser igual."
            return
        fig, ax = plt.subplots()
        ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        grafica_imagen.src_base64 = img_base64
        resultado_texto.value = ""
        page.update()

    bntGenerar = ft.ElevatedButton("Generar Gráfica de Pastel", on_click=generar_grafica)
    
    content = ft.Column(
        [
            etiquetas_input,
            valores_input,
            bntGenerar,
            resultado_texto,
            grafica_imagen,
        ],
        spacing=10,
    )
    return content

# Tema 4: Gráfica de Serie de Tiempo
def tema4(page):
    valores_x = ft.TextField(label="Valores X (separados por comas)", width=300)
    valores_y = ft.TextField(label="Valores Y (separados por comas)", width=300)
    resultado_texto = ft.Text()
    grafica_imagen = ft.Image(src="", width=500, height=400)

    def generar_grafica(e):
        try:
            x_vals = list(map(int, valores_x.value.split(",")))
            y_vals = list(map(int, valores_y.value.split(",")))
            if len(x_vals) != len(y_vals):
                resultado_texto.value = "Error: Los valores X y Y deben tener la misma longitud."
                return
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals)
            ax.set_xlabel("Tiempo")
            ax.set_ylabel("Valor")
            ax.set_title("Gráfica de Serie de Tiempo")
            ax.grid(True)
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            grafica_imagen.src_base64 = img_base64
            resultado_texto.value = ""
            page.update()
        except ValueError:
            resultado_texto.value = "Error: Ingresa solo números enteros para los valores de X e Y."
            page.update()

    bntGenerar = ft.ElevatedButton("Generar Gráfica de Serie de Tiempo", on_click=generar_grafica)
    
    content = ft.Column(
        [
            valores_x,
            valores_y,
            bntGenerar,
            resultado_texto,
            grafica_imagen,
        ],
        spacing=10,
    )
    return content

# Tema 5: Histogramas y Polígonos de Frecuencia
def tema5(page):
    input_data = ft.TextField(label="Datos (separados por comas)", width=300)
    resultado_texto = ft.Text()
    grafica_imagen = ft.Image(src="", width=500, height=400)

    def generar_grafica(e):
        try:
            data = list(map(float, input_data.value.split(",")))
            fig, ax = plt.subplots()
            ax.hist(data, bins=10, edgecolor="black", alpha=0.7)
            ax.set_xlabel("Valor")
            ax.set_ylabel("Frecuencia")
            ax.set_title("Histograma")
            ax.grid(True)
            buffer = io.BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            grafica_imagen.src_base64 = img_base64
            resultado_texto.value = ""
            page.update()
        except ValueError:
            resultado_texto.value = "Error: Ingresa solo números para generar el histograma."
            page.update()

    bntGenerar = ft.ElevatedButton("Generar Histograma", on_click=generar_grafica)
    
    content = ft.Column(
        [
            input_data,
            bntGenerar,
            resultado_texto,
            grafica_imagen,
        ],
        spacing=10,
    )
    return content

# Configuración de la página principal
def main(page):
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Tema 1: Tabla de Frecuencias", content=tema1(page)),
            ft.Tab(text="Tema 2: Gráfica de Barras", content=tema2(page)),
            ft.Tab(text="Tema 3: Gráfica de Pastel", content=tema3(page)),
            ft.Tab(text="Tema 4: Serie de Tiempo", content=tema4(page)),
            ft.Tab(text="Tema 5: Histograma", content=tema5(page)),
        ],
    )

    page.add(tabs)


