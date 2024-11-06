import flet as ft
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter
from Tema1_2 import tema1, tema2, tema3, tema4, tema5  # Importamos las funciones de Tema1_2
from Tema7_8 import Tema7_8

class UI(ft.UserControl):  # Considera cambiar UserControl en futuras actualizaciones

    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page
        self.instanciaTab = Tema7_8()
         
        # Gradiente de color para el diseño
        self.gradient_color = ft.LinearGradient(
            colors=["#007BFF", "#0066A2", "#003366"], 
            begin=ft.Alignment(0, 0),
            end=ft.Alignment(1, 0),
            stops=[0.0, 0.5, 1.0]
        )

        # Modo oscuro/claro
        self.mode_switch = ft.Switch(
            value=True,
            on_change=self.switch_update,
            thumb_color="black",
            thumb_icon={
                ft.ControlState.DEFAULT: ft.icons.LIGHT_MODE,
                ft.ControlState.SELECTED: ft.icons.DARK_MODE
            }
        )

        # Creación de las pestañas para `Tema1_2` dentro de `initial_container`
        tema1_2_tabs = ft.Tabs(
            tabs=[
                ft.Tab(text="Tema 1: Tabla de Frecuencias", content=tema1(self.page)),
                ft.Tab(text="Tema 2: Gráfica de Barras", content=tema2(self.page)),
                ft.Tab(text="Tema 3: Gráfica de Pastel", content=tema3(self.page)),
                ft.Tab(text="Tema 4: Serie de Tiempo", content=tema4(self.page)),
                ft.Tab(text="Tema 5: Histograma", content=tema5(self.page)),
            ],
            selected_index=0
        )

        # Contenedor inicial con pestañas de Tema1_2
        self.initial_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Tema 1 y 2", color="black"),
                    tema1_2_tabs,
                ]
            )
        )

        # Contenedores adicionales (sin cambios)
        self.tema3_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Tema 3 y 4", color="black"),
                    ft.Container(border_radius=20)
                ]
            )
        )

        self.tema5_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Tema 5 y 6", color="black"),
                    ft.Container(border_radius=20)
                ]
            )
        )

        # Contenedor para Tema7_8
        tema7_8_tabs = ft.Tabs(
            tabs=[
                self.instanciaTab.tab_evento(),
                self.instanciaTab.tab_aditiva(),
                self.instanciaTab.tab_condicional(),
                self.instanciaTab.tab_independientes(),
                self.instanciaTab.tab_regla_multiplicativa(),
            ]
        )

        self.container = ft.Column(
            controls=[tema7_8_tabs],
            scroll=ft.ScrollMode.ALWAYS,
            expand=True
        )

        self.tema9_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Tema 9 y 10", color="black"),
                    ft.Container(border_radius=20)
                ]
            )
        )

        # Lista de contenedores
        self.container_list = [
            self.initial_container, 
            self.tema3_container, 
            self.tema5_container, 
            self.container,
            self.tema9_container 
        ]

        # Contenedor dinámico para mostrar según el índice de `NavigationRail`
        self.container_1 = ft.Container(content=self.container_list[0], expand=True)

        # Navegación
        self.navigation_container = ft.Container(
            col=1,
            gradient=self.gradient_color,
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=True,
                        gradient=self.gradient_color, 
                        content=ft.NavigationRail(
                            bgcolor=ft.colors.TRANSPARENT,
                            expand=True,
                            on_change=self.change_page,
                            selected_index=0,
                            destinations=[
                                ft.NavigationBarDestination(icon=ft.icons.HOME),
                                ft.NavigationBarDestination(icon=ft.icons.ADD),
                                ft.NavigationBarDestination(icon=ft.icons.REMOVE),
                                ft.NavigationBarDestination(icon=ft.icons.CLOSE),
                                ft.NavigationBarDestination(icon=ft.icons.PERCENT),
                            ]
                        )
                    ),
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            expand=True,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.IconButton(icon=ft.icons.OUTPUT),
                                self.mode_switch
                            ]
                        )
                    ),
                ]
            )
        )

        # Frame que contiene `container_1`
        self.frame_2 = ft.Container(
            col=11,
            expand=True,
            content=self.container_1
        )

        # Estructura de la UI
        self.container = ft.ResponsiveRow(
            controls=[self.navigation_container, self.frame_2]
        )

    def change_page(self, e):
        index = e.control.selected_index
        self.container_1.content = self.container_list[index]
        self.frame_2.content = self.container_1
        self.update()
        print(index)

    def switch_update(self, e):
        self.page.theme_mode = "dark" if e.control.value else "light"
        self.page.update()

    def build(self):
        return self.container


def main(page: ft.Page):
    page.window.min_height = 820
    page.window.min_width = 510
    page.theme = ft.Theme(font_family="Open Sans")
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.add(UI(page))

ft.app(main)
