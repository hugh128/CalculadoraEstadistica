import flet as ft
import math
from collections import Counter

class Tema5_6:
    def __init__(self):
        # Espacio Muestral
        self.espacio_muestral_input = ft.TextField(label="Espacio Muestral (separado por comas)")
        self.espacio_muestral_output = ft.Text(value="")

        # Eventos
        self.evento1_input = ft.TextField(label="Evento 1 (separado por comas)")
        self.evento2_input = ft.TextField(label="Evento 2 (separado por comas)")
        self.union_output = ft.Text(value="")
        self.interseccion_output = ft.Text(value="")
        self.complemento_output = ft.Text(value="")

        # Permutación y Combinación
        self.n_input = ft.TextField(label="Valor de n", width=150)
        self.r_input = ft.TextField(label="Valor de r", width=150)
        self.permutacion_output = ft.Text(value="")
        self.permutacion_repeticion_output = ft.Text(value="")
        self.combinacion_output = ft.Text(value="")
        self.combinacion_repeticion_output = ft.Text(value="")

        # Permutación con Repetición - Nueva entrada para elementos
        self.total_n_input = ft.TextField(label="Total de elementos (n)")
        self.repeticiones_input = ft.TextField(label="Repeticiones (separadas por comas)")
        self.resultado_permutacion_repeticion = ft.Text(value="")

    # Métodos de cálculo
    def calcular_espacio_muestral(self, e):
        espacio = set(self.espacio_muestral_input.value.split(","))
        self.espacio_muestral_output.value = f"Espacio Muestral: {list(espacio)}"
        self.espacio_muestral_output.update()

    def calcular_union_eventos(self, e):
        evento1 = set(self.evento1_input.value.split(","))
        evento2 = set(self.evento2_input.value.split(","))
        union = sorted(list(set(evento1) | set(evento2)))
        self.union_output.value = f"Unión: {union}"
        self.union_output.update()

    def calcular_interseccion_eventos(self, e):
        evento1 = set(self.evento1_input.value.split(","))
        evento2 = set(self.evento2_input.value.split(","))
        interseccion = sorted(list(set(evento1) & set(evento2)))
        self.interseccion_output.value = f"Intersección: {interseccion}"
        self.interseccion_output.update()

    def calcular_complemento_evento(self, e):
        espacio = set(self.espacio_muestral_input.value.split(","))
        evento1 = set(self.evento1_input.value.split(","))
        complemento = sorted(list(set(espacio) - set(evento1)))
        self.complemento_output.value = f"Complemento de Evento 1: {complemento}"
        self.complemento_output.update()

    # Permutación normal
    def calcular_permutacion(self, e):
        try:
            n = int(self.n_input.value)
            r = int(self.r_input.value)
            permutacion_result = math.perm(n, r) if r <= n else "Error: r debe ser menor o igual a n."
            self.permutacion_output.value = f"Permutaciones (P({n}, {r})): {permutacion_result}"
            self.permutacion_output.update()
        except ValueError:
            self.permutacion_output.value = "Por favor, ingresa valores válidos para n y r."
            self.permutacion_output.update()

    # Permutación con repetición
    def calcular_permutacion_repeticion(self, e):
        try:
            n = int(self.total_n_input.value)  # Total de elementos
            repeticiones = list(map(int, self.repeticiones_input.value.split(",")))  # Repeticiones de cada elemento
            denominador = math.prod(math.factorial(r) for r in repeticiones)
            resultado = math.factorial(n) // denominador
            self.resultado_permutacion_repeticion.value = f"Permutación con Repetición: {resultado}"
            self.resultado_permutacion_repeticion.update()
        except ValueError:
            self.resultado_permutacion_repeticion.value = "Por favor, ingresa valores válidos para n y repeticiones."
            self.resultado_permutacion_repeticion.update()

    # Combinación normal
    def calcular_combinacion(self, e):
        try:
            n = int(self.n_input.value)
            r = int(self.r_input.value)
            combinacion_result = math.comb(n, r) if r <= n else "Error: r debe ser menor o igual a n."
            self.combinacion_output.value = f"Combinaciones (C({n}, {r})): {combinacion_result}"
            self.combinacion_output.update()
        except ValueError:
            self.combinacion_output.value = "Por favor, ingresa valores válidos para n y r."
            self.combinacion_output.update()

    # Combinación con repetición
    def calcular_combinacion_repeticion(self, e):
        try:
            n = int(self.n_input.value)
            r = int(self.r_input.value)
            combinacion_repeticion_result = math.comb(n + r - 1, r)  # Fórmula para combinaciones con repetición
            self.combinacion_repeticion_output.value = f"Combinaciones con Repetición (C({n} con repetición, {r})): {combinacion_repeticion_result}"
            self.combinacion_repeticion_output.update()
        except ValueError:
            self.combinacion_repeticion_output.value = "Por favor, ingresa valores válidos para n y r."
            self.combinacion_repeticion_output.update()

    # Pestañas de interfaz para Espacio Muestral y Eventos
    def tab_espacio_muestral(self):
        return ft.Tab(
            text="Espacio Muestral y Eventos",
            content=ft.Column([
                self.espacio_muestral_input,
                self.espacio_muestral_output,
                self.evento1_input,
                self.evento2_input,
                ft.ElevatedButton("Calcular Unión", on_click=self.calcular_union_eventos),
                self.union_output,
                ft.ElevatedButton("Calcular Intersección", on_click=self.calcular_interseccion_eventos),
                self.interseccion_output,
                ft.ElevatedButton("Calcular Complemento de Evento 1", on_click=self.calcular_complemento_evento),
                self.complemento_output,
            ])
        )

    # Pestañas separadas para Permutación y Combinación
    def tab_permutacion_normal(self):
        return ft.Tab(
            text="Permutación Normal",
            content=ft.Column([
                self.n_input,
                self.r_input,
                ft.ElevatedButton("Calcular Permutación", on_click=self.calcular_permutacion),
                self.permutacion_output,
            ])
        )

    def tab_permutacion_repeticion(self):
        return ft.Tab(
            text="Permutación con Repetición",
            content=ft.Column([
                self.total_n_input,
                self.repeticiones_input,
                ft.ElevatedButton("Calcular Permutación con Repetición", on_click=self.calcular_permutacion_repeticion),
                self.resultado_permutacion_repeticion,
            ])
        )

    def tab_combinacion_normal(self):
        return ft.Tab(
            text="Combinación Normal",
            content=ft.Column([
                self.n_input,
                self.r_input,
                ft.ElevatedButton("Calcular Combinación", on_click=self.calcular_combinacion),
                self.combinacion_output,
            ])
        )

    def tab_combinacion_repeticion(self):
        return ft.Tab(
            text="Combinación con Repetición",
            content=ft.Column([
                self.n_input,
                self.r_input,
                ft.ElevatedButton("Calcular Combinación con Repetición", on_click=self.calcular_combinacion_repeticion),
                self.combinacion_repeticion_output,
            ])
        )
