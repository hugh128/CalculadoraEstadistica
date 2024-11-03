import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora de Probabilidades"
    page.bgcolor = ft.colors.WHITE
    page.scroll = "adaptive"
      # Mostrar un saludo en la parte superior
    saludo = ft.Text("PROBABILIDADES", size=24, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)

    #-----------------------------------------------------------------FUNCIONES-------------------------------------------------
    # Función para calcular la probabilidad de un evento
    def calcular_probabilidad(e):
        try:
            eventos_exitosos = float(input_eventos_exitosos.value)
            total_eventos = float(input_total_eventos.value)
            probabilidad = eventos_exitosos / total_eventos
            resultado_probabilidad.value = f"P(E) = {probabilidad:.2f} (o {probabilidad * 100:.2f}%)"
        except (ValueError, ZeroDivisionError):
            resultado_probabilidad.value = "Error: ingresa valores válidos."
        page.update()

    # Función para calcular la probabilidad aditiva
    def calcular_probabilidad_aditiva(e):
        try:
            prob_a = float(input_prob_a.value)
            prob_b = float(input_prob_b.value)
            prob_interseccion = float(input_prob_interseccion.value)
            prob_union = prob_a + prob_b - prob_interseccion
            resultado_aditiva.value = f"P(A ∪ B) = {prob_union:.2f} (o {prob_union * 100:.2f}%)"
        except (ValueError, ZeroDivisionError):
            resultado_aditiva.value = "Error: ingresa valores válidos."
        page.update()

    # Función para calcular la probabilidad condicional
    def calcular_probabilidad_condicional(e):
        try:
            p_ab = float(prob_evento_conjunto.value)  # P(A ∩ B)
            p_b = float(prob_evento_b.value)          # P(B)

            if p_b == 0:
                resultado_condicional.value = "P(B) no puede ser 0."
            else:
                # Calcular la probabilidad condicional
                p_a_given_b = p_ab / p_b
                resultado_condicional.value = f"Probabilidad condicional P(A|B): {p_a_given_b:.4f}"
        except ValueError:
            resultado_condicional.value = "Por favor, ingresa valores válidos."
        page.update()

    def calcularEventosIndependientes(event):
        try:
            p1 = float(prob_event1.value)
            p2 = float(prob_event2.value)

            # Calcular la probabilidad de que ambos eventos ocurran
            prob_ambos = p1 * p2
            resultadoEventosIndependientes.value = f"Probabilidad de que ambos eventos ocurran: {prob_ambos:.4f}"
        except ValueError:
            resultadoEventosIndependientes.value = "Por favor, ingresa valores válidos."

        page.update()
    # Crear las pestañas
    tabs = ft.Tabs()
    
    def calcularReglaMultiplicativa(event):
        try:
            p_a = float(prob_evento1.value)
            p_b = float(prob_evento2.value)

            # Calcular la probabilidad de que ambos eventos ocurran
            prob_ambos = p_a * p_b
            resultado.value = f"Probabilidad de que ambos eventos ocurran (P(A ∩ B)): {prob_ambos:.4f}"
        except ValueError:
            resultado.value = "Por favor, ingresa valores válidos."

        page.update()
    def barra():
        return ft.Container(
                content=ft.Text("", text_align=ft.MainAxisAlignment.CENTER),
                margin=0,
                padding=7,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_200,
                border_radius=10,
            )
    #-------------------------------------------------------------PESTAÑAS-----------------------------------------------------
    # Pestaña: Probabilidad de un Evento
    tab_evento = ft.Tab(
        text="Probabilidad de un Evento",
            content=ft.Column([
            barra(),
            ft.Container(
                content= ft.Column([
                    ft.Text("Si un experimento puede dar como resultado cualquiera de  N diferentes resultados que  tienen  las  mismas  probabilidades  de  ocurrir,  y  si  exactamente  n de  estos resultados corresponden al evento A, entonces la probabilidad del evento A es",width=800),
                    ft.Image(
                    src="assets/Probabilidad.png",
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN,
                    
                    ),
                    ft.Text("Ejemplo:",weight=ft.FontWeight.BOLD),
                    ft.Text("A una  clase  de  estadística  para  ingenieros  asisten  25  estudiantes  de  ingeniería  industrial,  10  de ingeniería mecánica, 10 de ingeniería eléctrica y 8 de ingeniería civil. Si el profesor elige al azar a un estudiante para que conteste una pregunta, ¿qué probabilidades hay de que el elegido sea a) estudiante de ingeniería industrial, b) estudiante de ingeniería civil o estudiante de ingeniería eléctrica?. "),
                    ft.Text("Solución:",weight = ft.FontWeight.BOLD),
                    ft.Text("Las especialidades de los estudiantes de ingeniería industrial, mecánica, eléctrica y civil se denotan con I, M, E y C, respectivamente. El grupo está integrado por 53 estudiantes y todos tienen las mismas probabilidades de ser seleccionados. "),
                    ft.Text("a) Como 25 de los 53 individuos estudian ingeniería industrial, la probabilidad del evento I, es decir, la de elegir al azar a alguien que estudia ingeniería industrial, es"),
                    ft.Text("P(I)= 25/53 = 0.471"),
                    ft.Text("b) Como 10 + 8 = 18 de los 53 estudiantes son de las especialidades de ingeniería civil o eléctrica,  se deduce que"),
                    ft.Text("P(C U E) = 18/53 = 0.339"),
                ]),
                
                margin=0,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_100,
                height=470,
                border_radius=10,
                
            ),
            barra(),
            input_eventos_exitosos := ft.TextField(label="Eventos Exitosos", keyboard_type=ft.KeyboardType.NUMBER),
            input_total_eventos := ft.TextField(label="Total de Eventos", keyboard_type=ft.KeyboardType.NUMBER),
            ft.ElevatedButton(text="Calcular P(E)", on_click=calcular_probabilidad),
            resultado_probabilidad := ft.Text(""),
        ]),

    )
    #------------------------------------------------------------------------------------------------------------------
    # Pestaña: Regla Aditiva
    tab_aditiva = ft.Tab(
        text="Regla Aditiva",
        content=ft.Column([
            barra(),
            ft.Container(
                content= ft.Column([
                    ft.Text("Si A y B son dos eventos no excluyentes, entonces",width=400),
                    ft.Image(
                    src="assets/aditiva.png",
                    width=300,
                    height=300,
                    fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Text("Ejemplo: ",weight = ft.FontWeight.BOLD),
                    ft.Text("Al final del semestre John se va a graduar en la facultad de ingeniería industrial de una universidad. Después de tener entrevistas en dos empresas en donde quiere trabajar, determina que la probabilidad que tiene de lograr una oferta de empleo en la empresa A es 0.8, y que la probabilidad de obtenerla en  la empresa B es 0.6. Si, por otro lado, considera que la probabilidad de recibir ofertas de ambas empresas es 0.5, ¿qué probabilidad tiene de obtener al menos una oferta de esas dos empresas?"),
                    ft.Text("Solución: ",weight = ft.FontWeight.BOLD),
                    ft.Text("P(A U B) = P(A) + P(B) - P(A ∩ B) = 0.8 + 0.6 - 0.5 = 0.9"),
                ]),
                
                margin=0,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_100,
                height=515,
                border_radius=10,
                
            ),
            barra(),
            input_prob_a := ft.TextField(label="Probabilidad de A (P(A))", keyboard_type=ft.KeyboardType.NUMBER),
            input_prob_b := ft.TextField(label="Probabilidad de B (P(B))", keyboard_type=ft.KeyboardType.NUMBER),
            input_prob_interseccion := ft.TextField(label="Probabilidad de A ∩ B (P(A ∩ B))", keyboard_type=ft.KeyboardType.NUMBER),
            ft.ElevatedButton(text="Calcular P(A ∪ B)", on_click=calcular_probabilidad_aditiva),
            resultado_aditiva := ft.Text(""),
        ])
    )
    #------------------------------------------------------------------------------------------------------------------
 # Probabilidad condicional
    tab_condicional = ft.Tab(
        text="Probabilidad condicional",
        content=ft.Column([
            barra(),
            ft.Container(
                content= ft.Column([
                    ft.Text("Definición 1: La probabilidad condicional de B, dado A, que se denota con P(B|A), siempre que P(A)>0, se define como"), 
                    ft.Image(
                        src="assets/condicional.png",
                        width=150,
                        height=100,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Text("Ejemplo: ", weight = ft.FontWeight.BOLD),
                    ft.Text("La  probabilidad  de  que  un  vuelo  programado  normalmente  salga  a  tiempo  es  P(D)  =  0.83,  la probabilidad de que llegue a tiempo es P(A) = 0.82 y la probabilidad de que salga y llegue a tiempo es  P(D ∩ A) = 0.78. Calcule la probabilidad de que un avión a) llegue a tiempo, dado que salió a tiempo; y b) salió a tiempo, dado que llegó a tiempo."),
                    ft.Text("Solución: ",weight = ft.FontWeight.BOLD),
                    ft.Text("a) La probabilidad de que un avión llegue a tiempo, dado que salió a tiempo es \n P(A|D) = P(D ∩ A)/P(D) = 0.78/0.83 = 0.94"),
                    ft.Text("b) La probabilidad de que un avión haya salido a tiempo, dado que llegó a tiempo es \n P(D|A) = P(D ∩ A)/P(A) = 0.78/0.82 = 0.95"),
                #text_align=ft.MainAxisAlignment.CENTER
                ]),
                height=375,
                margin=0,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_100,
                border_radius=10,
            ),
            barra(),
            prob_evento_conjunto := ft.TextField(label="Probabilidad de P(A ∩ B)", keyboard_type=ft.KeyboardType.NUMBER),
            prob_evento_b := ft.TextField(label="Probabilidad de P(B)", keyboard_type=ft.KeyboardType.NUMBER),
            ft.ElevatedButton(text="Calcular la probabilidad condicional", on_click=calcular_probabilidad_condicional),
            resultado_condicional := ft.Text("", size=20)  # Para mostrar el resultado
        ])
    )
    #------------------------------------------------------------------------------------------------------------------
        # Pestaña: Eventos independientes
    tab_independientes = ft.Tab(
        text="Eventos independientes",
        content=ft.Column([
            barra(),
            ft.Container(
                content= ft.Column([
                ft.Text("Dos eventos A y B son independientes si y sólo si"),
                ft.Text("P(B|A) = P(B) o P(A|B) = P(A)", weight = ft.FontWeight.BOLD),
                ft.Text("si se asume la existencia de probabilidad condicional. De otra forma, A y B son dependientes"),
                ft.Text("Consideremos ahora un experimento en el que se sacan 2 cartas, una después de la otra, de una baraja ordinaria, con reemplazo. Los eventos se definen como "),
                ft.Text("A: la primera carta es un trebol,"),
                ft.Text("B: la segunda carta es una espada."),
                ft.Text("Como la primera carta se reemplaza, nuestro espacio muestral para la primera y segunda cartas consta de 52 cartas, que contienen 13 treboles y 13 espadas. Entonces,"),
                ft.Text("P(B|A) = 13/52 = 1/4   y   P(B) = 13/52 = 1/4"),
                ft.Text("Es decir, P(B|A) = P(B). Cuando esto es cierto, se dice que los eventos A y B son independientes."),

                ]),

                margin=0,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_100,
                height = 300,
                border_radius=10,
            ),
            barra(),
            prob_event1 := ft.TextField(label="Probabilidad del evento 1 P(A)", keyboard_type=ft.KeyboardType.NUMBER),
            prob_event2 := ft.TextField(label="Probabilidad del evento 2 P(B)", keyboard_type=ft.KeyboardType.NUMBER),
            ft.ElevatedButton(text="Calcular P(B|A)", on_click=calcularEventosIndependientes),
            resultadoEventosIndependientes := ft.Text(""),
        ])
    )
    #------------------------------------------------------------------------------------------------------------------
    # Pestaña: Regla multiplicativa
    tab_regla_multiplicativa = ft.Tab(
        text="Regla del producto",
        content=ft.Column([
            barra(),
            ft.Container(
                content= ft.Column([
                ft.Text("Si en un experimento pueden ocurrir los eventos A y B, entonces"),
                ft.Text("P(A ∩ B) = P(A) * P(B|A)",weight = ft.FontWeight.BOLD),
                ft.Text("siempre que P(A)>0",weight = ft.FontWeight.BOLD),
                ft.Text("Por consiguiente, la probabilidad de que ocurran A y B es igual a la probabilidad de que ocurra A multiplicada por la probabilidad condicional de que ocurra B, dado que ocurre A. Como los eventos A ∩ B y B ∩ A son equivalentes, del teorema 1 se deduce que también podemos escribir"),
                ft.Text("P(A ∩ B) = P(B ∩ A) = P(B) * P(A|B)",weight = ft.FontWeight.BOLD),
                ft.Text("En otras palabras, no importa qué evento se considere como A ni qué evento se considere como B."),
                ft.Text("Ejemplo: ",weight = ft.FontWeight.BOLD),
                ft.Text("Supongamos que tenemos dos eventos independientes: "),
                ft.Text("Evento A: Lanzar un dado y que salga un 4. La probabilidad de que esto ocurra es P(A)=1/6 \nEvento B: Lanzar una moneda y que salga cara. La probabilidad de que esto ocurra es P(B)=1/2"),
                ft.Text("Queremos calcular la probabilidad de que ambos ocurran, es decir, P(A ∩ B)"),
                ft.Text("Solución: ",weight = ft.FontWeight.BOLD),
                ft.Text("La regla del producto establece que si A y B son eventos independientes, entoces: P(A ∩ B) = P(A) * P(B)"),
                ft.Text("Sustituyendo las probabilidades que tenemos: P(A ∩ B) = P(A)*P(B) = (1/6)*(1/2) = 1/12 )= 0.083 \nLa probabilidad de que al lanzar un dado salga un 4 y al lanzar una moneda salga cara es 1/12."),
                ]),

                margin=0,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_100,
                height = 500,
                border_radius=10,
            ),
            barra(),
            prob_evento1 := ft.TextField(label="Probabilidad del evento 1 P(A)", keyboard_type=ft.KeyboardType.NUMBER),
            prob_evento2 := ft.TextField(label="Probabilidad del evento 2 P(B)", keyboard_type=ft.KeyboardType.NUMBER),
            ft.ElevatedButton(text="Calcular P(A ∩ B)", on_click=calcularReglaMultiplicativa),
            resultado := ft.Text(""),
        ])
    )
    # Crear pestañas
    tabs = ft.Tabs(
        #expand=1,
        tabs=[
        tab_evento,
        tab_aditiva,
        tab_condicional,
        tab_independientes,
        tab_regla_multiplicativa,
        ])

    # Agregar el saludo y las pestañas a la página
    saludo = ft.Text("Bienvenido a la calculadora de probabilidades", size=20, text_align=ft.MainAxisAlignment.CENTER)
    page.add(saludo, tabs)

# Ejecutar la aplicación
ft.app(target=main)
















    # Agregar las pestañas al contenedor
    #tabs.tabs.extend([tab_evento, tab_aditiva, tab_condicional])

    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Agregar las pestañas a la página
    #page.add(saludo,tabs)

    

# Ejecutar la aplicación
#ft.app(target=main)
