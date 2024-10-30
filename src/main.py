import flet as ft

class UI(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

      
        self.gradient_color = ft.LinearGradient(
            colors=["#007BFF", "#0066A2", "#003366"], 
            begin=ft.Alignment(0, 0),        # Izquierda
            end=ft.Alignment(1, 0),          # Derecha
            stops=[0.0, 0.5, 1.0]  # Aumentar el número de stops para una transición más suave
        )

        self.mode_switch = ft.Switch(
            value=True,
            on_change= self.switch_update,
            thumb_color="black",
            thumb_icon={
                ft.MaterialState.DEFAULT: ft.icons.LIGHT_MODE,
                ft.MaterialState.SELECTED: ft.icons.DARK_MODE
            }
        )

        self.initial_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,  # Hacer que el initial_container se expanda
            content=ft.Column(
                controls=[
                    ft.Text("Tema 1 y 2", color="black"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        self.tema3_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,  # Hacer que el initial_container se expanda
            content=ft.Column(
                controls=[
                    ft.Text("Tema 3 y 4", color="black"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        self.tema5_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,  # Hacer que el initial_container se expanda
            content=ft.Column(
                controls=[
                    ft.Text("Tema 5 y 6", color="black"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        self.tema7_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,  # Hacer que el initial_container se expanda
            content=ft.Column(
                controls=[
                    ft.Text("Tema 7 y 8", color="black"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )

        self.tema9_container = ft.Container(
            bgcolor="#F0F0F0",
            border_radius=20,
            padding=20,
            expand=True,  # Hacer que el initial_container se expanda
            content=ft.Column(
                controls=[
                    ft.Text("Tema 9 y 10", color="black"),
                    ft.Container(
                        border_radius=20,
                    )
                ]
            )
        )





        self.container_list = [
                            self.initial_container, 
                            self.tema3_container, 
                            self.tema5_container, 
                            self.tema7_container, 
                            self.tema9_container ]

        self.container_1 = ft.Container(content=self.container_list[0], expand=True)

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
                            selected_index= 0,
                            destinations=[
                                ft.NavigationDestination(
                                    icon=ft.icons.HOME,
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.ADD,
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.REMOVE,
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.CLOSE,
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.PERCENT,
                                ),
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
                                ft.IconButton(
                                    icon=ft.icons.OUTPUT,
                                ),
                                self.mode_switch
                            ]
                        )
                    ),
                ]
            )
        )

        self.frame_2 = ft.Container(
            col=11,
            expand=True,  # Hacer que el frame_2 se expanda
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
        self.container_1.content = self.container_list[index]
        self.frame_2.content = self.container_1
        self.update()
        print(index)

    def switch_update(self, e):
        if e.control.value :
            self.page.theme_mode = "dark"
        else:
            self.page.theme_mode = "light"
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
