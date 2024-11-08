import flet as ft
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter
from io import BytesIO

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
            # Convertir los valores ingresados a flotantes
            numbers = [float(num.strip()) for num in number_input.value.split(",") if num.strip()]
            number_list.extend(numbers)
            number_input.value = ""
            result_area.value = "Números ingresados: " + ", ".join(map(str, number_list))
        except ValueError:
            result_area.value = "Por favor ingresa números válidos separados por comas."
        page.update()

    def sort_numbers(e):
        if number_list:
            # Ordenar la lista de números
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

            for number, freq in sorted(number_counter.items()):
                relative_frequency = freq / total_numbers
                cumulative_frequency += relative_frequency
                table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(f"{number:.2f}")),
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




#grafica barras
def tema2(page):
    # Campos de entrada para los datos
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
            
            # Guardar la gráfica en un buffer en formato base64
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

    # Botón para generar la gráfica
    bntGenerar = ft.ElevatedButton("Generar Gráfica", on_click=generar_grafica)
    
    # Contenedor de desplazamiento para los datos y la gráfica
    scrollable_content = ft.Column(
        [
            datos_x,
            datos_y,
            bntGenerar,
            resultado_texto,
            grafica_imagen,
        ],
        spacing=10,
        scroll="always",  # Activar desplazamiento
        width=550,  # Ajustar ancho si es necesario
        height=450,  # Ajustar alto para el área de visualización deseada
    )
    
    # Contenedor principal
    content = ft.Container(
        content=scrollable_content,
        padding=10,
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
    datos_input = ft.TextField(label="Datos (separados por comas)", width=300)
    intervalos_input = ft.TextField(label="Número de Intervalos", width=300)
    tabla_resultado = ft.Column()
    grafico_histograma = ft.Container()
    grafico_polinomio = ft.Container()

    def generar_grafica(e):
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

        # Convertir la figura a imagen y mostrarla
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        grafico_histograma.content = ft.Image(src_base64=img_base64)

    # Función para graficar el polígono de frecuencias
    def graficar_poligono(marcas, frecuencias):
        fig, ax = plt.subplots()
        ax.plot(marcas, frecuencias, marker="o", color="royalblue", linestyle="-", linewidth=2, markersize=6)
        ax.set_xlabel("Marca de Clase")
        ax.set_ylabel("Frecuencia")
        ax.set_title("Polígono de Frecuencias")
        ax.grid(True, linestyle="--", alpha=0.7)

        # Convertir la figura a imagen y mostrarla
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        grafico_polinomio.content = ft.Image(src_base64=img_base64)

    bntGenerar = ft.ElevatedButton("Generar Histograma y Polígono", on_click=generar_grafica)
    
    content = ft.Column(
        [
            datos_input,
            intervalos_input,
            bntGenerar,
            tabla_resultado,
            grafico_histograma,
            grafico_polinomio,
        ],
        spacing=10,
    )

    return content

    
  

