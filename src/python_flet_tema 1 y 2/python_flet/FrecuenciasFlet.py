import flet as ft
from collections import Counter

def main(page: ft.Page):
    # Lista para almacenar los números
    number_list = []

    # Etiqueta de instrucciones
    instruction_label = ft.Text("Ingresa un número y presiona 'Agregar'")

    # Campo de entrada de números
    number_input = ft.TextField(label="Número", keyboard_type="number", width=150)

    # Área de resultados para mostrar los números ingresados o el resultado de ordenación
    result_area = ft.Text()

    # Tabla de frecuencias
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Número"), ),
            ft.DataColumn(ft.Text("Frecuencia")),
            ft.DataColumn(ft.Text("Frecuencia Relativa")),
            ft.DataColumn(ft.Text("Frecuencia Acumulada")),
            ft.DataColumn(ft.Text("Total Acumulado")),
        ],
        rows=[],
    
    )

    def add_number(e):
        try:
            number = int(number_input.value)
            number_list.append(number)
            number_input.value = ""
            result_area.value = "Números ingresados: " + ", ".join(map(str, number_list))
        except ValueError:
            result_area.value = "Por favor ingresa un número válido."
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
            # Limpiar la tabla antes de llenarla
            table.rows.clear()

            # Contar la frecuencia de cada número
            number_counter = Counter(number_list)
            total_numbers = len(number_list)

            # Variables para acumulados
            cumulative_frequency = 0.0
            cumulative_total = 0

            # Llenar la tabla con los datos calculados
            for number, freq in number_counter.items():
                relative_frequency = freq / total_numbers
                cumulative_frequency += relative_frequency
                cumulative_total += number * freq

                # Agregar fila a la tabla
                table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(number))),
                            ft.DataCell(ft.Text(str(freq))),
                            ft.DataCell(ft.Text(f"{relative_frequency:.4f}")),
                            ft.DataCell(ft.Text(f"{cumulative_frequency:.4f}")),
                            ft.DataCell(ft.Text(str(cumulative_total))),
                        ]
                    )
                )

            # Agregar fila con el total de datos ingresados
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Total de datos:")),
                        ft.DataCell(ft.Text(str(total_numbers))),
                        ft.DataCell(ft.Text("")),
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

    # Botones de acción
    add_button = ft.ElevatedButton("Agregar número", on_click=add_number)
    sort_button = ft.ElevatedButton("Ordenar números", on_click=sort_numbers)
    frequency_button = ft.ElevatedButton("Calcular frecuencia", on_click=calculate_frequency)
    clear_button = ft.ElevatedButton("Limpiar números", on_click=clear_numbers)

    # Añadir todos los elementos a la página
    page.add(
        instruction_label,
        number_input,
        add_button,
        sort_button,
        frequency_button,
        clear_button,
        result_area,
        table,
    )

# Ejecutar la aplicación en el servidor de Flet
ft.app(target=main)
