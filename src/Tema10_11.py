# Tema10_11.py

import flet as ft
from math import comb, factorial, exp
from functools import reduce

# Función para crear una barra de separación estilizada
def crear_barra_separacion():
    return ft.Container(
        content=ft.Divider(),
        width=300,
        height=1,
        padding=5
    )

# Pestaña para distribución binomial
def crear_pestana_binomial(page):
    n_input = ft.TextField(label="Número de ensayos (n)")
    p_input = ft.TextField(label="Probabilidad de éxito (p)")
    k_input = ft.TextField(label="Número de éxitos (k)")
    resultado_binomial = ft.Text(value="Resultado: ")

    calcular_btn = ft.ElevatedButton(
        text="Calcular",
        on_click=lambda e: calcular_binomial(n_input, p_input, k_input, resultado_binomial, page)
    )

    return ft.Column(
        [
            ft.Text("Distribución Binomial"),
            n_input,
            p_input,
            k_input,
            calcular_btn,
            resultado_binomial
        ]
    )

# Función de cálculo para la distribución binomial
def calcular_binomial(n_input, p_input, k_input, resultado_binomial, page):
    try:
        n = int(n_input.value)
        p = float(p_input.value)
        k = int(k_input.value)
        prob = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        resultado_binomial.value = f"Resultado: {prob:.4f}"
    except ValueError:
        resultado_binomial.value = "Error: Verifica los valores ingresados."
    page.update()

# Pestaña para distribución multinomial
def crear_pestana_multinomial(page):
    n_multinomial = ft.TextField(label="Número total de pruebas (n)")
    x_values = ft.TextField(label="Éxitos por categoría (x1, x2, ...)")
    p_values = ft.TextField(label="Probabilidades por categoría (p1, p2, ...)")
    resultado_multinomial = ft.Text(value="Resultado: ")

    calcular_btn_multinomial = ft.ElevatedButton(
        text="Calcular",
        on_click=lambda e: calcular_multinomial(n_multinomial, x_values, p_values, resultado_multinomial, page)
    )

    return ft.Column(
        [
            ft.Text("Distribución Multinomial"),
            n_multinomial,
            x_values,
            p_values,
            calcular_btn_multinomial,
            resultado_multinomial
        ]
    )

# Función de cálculo para la distribución multinomial
def calcular_multinomial(n_multinomial, x_values, p_values, resultado_multinomial, page):
    try:
        n = int(n_multinomial.value)
        x_list = list(map(int, x_values.value.split(',')))
        p_list = list(map(float, p_values.value.split(',')))

        if sum(x_list) != n or abs(sum(p_list) - 1) > 0.01:
            resultado_multinomial.value = "Error: Verifica que Σx = n y Σp = 1"
            page.update()
            return

        coeficiente = factorial(n) / reduce(lambda acc, x: acc * factorial(x), x_list, 1)
        probabilidad = coeficiente * reduce(lambda acc, xp: acc * (xp[1] ** xp[0]), zip(x_list, p_list), 1)
        resultado_multinomial.value = f"Resultado: {probabilidad:.4f}"
    except ValueError:
        resultado_multinomial.value = "Error: Verifica los valores ingresados."
    page.update()

# Pestaña para distribución hipergeométrica
def crear_pestana_hipergeometrica(page):
    N_input = ft.TextField(label="Población total (N)")
    K_input = ft.TextField(label="Éxitos en la población (K)")
    n_input_hyper = ft.TextField(label="Tamaño de la muestra (n)")
    k_input_hyper = ft.TextField(label="Éxitos en la muestra (k)")
    resultado_hipergeometrica = ft.Text(value="Resultado: ")

    calcular_btn = ft.ElevatedButton(
        text="Calcular",
        on_click=lambda e: calcular_hipergeometrica(N_input, K_input, n_input_hyper, k_input_hyper, resultado_hipergeometrica, page)
    )

    return ft.Column(
        [
            ft.Text("Distribución Hipergeométrica"),
            N_input,
            K_input,
            n_input_hyper,
            k_input_hyper,
            calcular_btn,
            resultado_hipergeometrica
        ]
    )

# Función de cálculo para la distribución hipergeométrica
def calcular_hipergeometrica(N_input, K_input, n_input_hyper, k_input_hyper, resultado_hipergeometrica, page):
    try:
        N = int(N_input.value)
        K = int(K_input.value)
        n = int(n_input_hyper.value)
        k = int(k_input_hyper.value)
        prob = (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
        resultado_hipergeometrica.value = f"Resultado: {prob:.4f}"
    except ValueError:
        resultado_hipergeometrica.value = "Error: Verifica los valores ingresados."
    page.update()

# Pestaña para distribución geométrica
def crear_pestana_geometrica(page):
    p_input_geo = ft.TextField(label="Probabilidad de éxito (p)")
    k_input_geo = ft.TextField(label="Número de ensayos hasta el primer éxito (k)")
    resultado_geometrica = ft.Text(value="Resultado: ")

    calcular_btn = ft.ElevatedButton(
        text="Calcular",
        on_click=lambda e: calcular_geometrica(p_input_geo, k_input_geo, resultado_geometrica, page)
    )

    return ft.Column(
        [
            ft.Text("Distribución Geométrica"),
            p_input_geo,
            k_input_geo,
            calcular_btn,
            resultado_geometrica
        ]
    )

# Función de cálculo para la distribución geométrica
def calcular_geometrica(p_input_geo, k_input_geo, resultado_geometrica, page):
    try:
        p = float(p_input_geo.value)
        k = int(k_input_geo.value)
        prob = p * ((1 - p) ** (k - 1))
        resultado_geometrica.value = f"Resultado: {prob:.4f}"
    except ValueError:
        resultado_geometrica.value = "Error: Verifica los valores ingresados."
    page.update()

# Pestaña para distribución de Poisson
def crear_pestana_poisson(page):
    lambda_input = ft.TextField(label="Tasa de éxito promedio (λ)")
    k_input_poisson = ft.TextField(label="Número de éxitos (k)")
    resultado_poisson = ft.Text(value="Resultado: ")

    calcular_btn = ft.ElevatedButton(
        text="Calcular",
        on_click=lambda e: calcular_poisson(lambda_input, k_input_poisson, resultado_poisson, page)
    )

    return ft.Column(
        [
            ft.Text("Distribución de Poisson"),
            lambda_input,
            k_input_poisson,
            calcular_btn,
            resultado_poisson
        ]
    )

# Función de cálculo para la distribución de Poisson
def calcular_poisson(lambda_input, k_input_poisson, resultado_poisson, page):
    try:
        lambd = float(lambda_input.value)
        k = int(k_input_poisson.value)
        prob = (lambd ** k * exp(-lambd)) / factorial(k)
        resultado_poisson.value = f"Resultado: {prob:.4f}"
    except ValueError:
        resultado_poisson.value = "Error: Verifica los valores ingresados."
    page.update()

