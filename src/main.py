import flet as ft
import subprocess

class UI(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

        self.gradient_color = ft.LinearGradient(
            colors=["#007BFF", "#0066A2", "#003366"], 
            begin=ft.Alignment(0, 0),
            end=ft.Alignment(1, 0),
            stops=[0.0, 0.5, 1.0]
        )

        self.mode_switch = ft.Switch(
            value=True,
            on_change=self.switch_update,
            thumb_color="black",
            thumb_icon={
                ft.MaterialState.DEFAULT: ft.icons.LIGHT_MODE,
                ft.MaterialState.SELECTED: ft.icons.DARK_MODE
            }
        )

        # Contenedor inicial
        self.initial_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Tema 1 y 2", color="black"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        # Otros contenedores
        self.tema3_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Tema 3 y 4", color="black"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        # Lista de contenedores
        self.container_list = [
            self.initial_container, 
            self.tema3_container,
            # Añadir los demás contenedores aquí
        ]

        self.container_1 = ft.Container(content=self.container_list[0], expand=True)

        # NavigationRail con evento para el icono de casa
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
                                ft.NavigationDestination(icon=ft.icons.HOME),
                                ft.NavigationDestination(icon=ft.icons.ADD),
                                ft.NavigationDestination(icon=ft.icons.REMOVE),
                                ft.NavigationDestination(icon=ft.icons.CLOSE),
                                ft.NavigationDestination(icon=ft.icons.PERCENT),
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

        self.frame_2 = ft.Container(
            col=11,
            expand=True,
            content=self.container_1
        )

        self.container = ft.ResponsiveRow(
            controls=[
                self.navigation_container,
                self.frame_2,
            ]
        )

    def change_page(self, e):
        index = e.control.selected_index
        if index == 0:
            # Abre ventana.py cuando se selecciona el icono de la casa
            subprocess.Popen(["python", "src/python_flet_tema 1 y 2/python_flet/ventana.py"])
        else:
            # Cambia de contenido en el frame para otros iconos
            self.container_1.content = self.container_list[index]
            self.frame_2.content = self.container_1
            self.update()

    def switch_update(self, e):
        self.page.theme_mode = "dark" if e.control.value else "light"
        self.page.update()

    def build(self):
        return self.container

def main(page: ft.Page):
    page.window_min_height = 820
    page.window_min_width = 510
    page.theme = ft.Theme(font_family="Open Sans")
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.add(UI(page))

ft.app(main)
