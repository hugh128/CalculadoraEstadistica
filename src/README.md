# CalculadoraEstadistica

# Calculadora Estadística y Probabilidad en Flet

Este proyecto es una calculadora de estadística desarrollada en Python utilizando la biblioteca [Flet](https://flet.dev/). La aplicación proporciona una interfaz gráfica para realizar cálculos estadísticos, crear gráficos y trabajar con distribuciones de probabilidad. Los temas están estructurados para facilitar la navegación y el análisis de datos.

## Estructura del Proyecto

El proyecto está organizado en módulos, cada uno de los cuales representa un tema de estadística. Estos módulos incluyen cálculos de medidas estadísticas, frecuencias, gráficos y distribuciones de probabilidad.

### Temas y Funcionalidades

#### Tema 1_2: Frecuencias y Gráficas Básicas

Este tema abarca la creación de tablas de frecuencias y gráficos básicos para visualizar datos.

1. **Tabla de Frecuencias**
   - Permite ingresar una lista de números para calcular:
     - Frecuencia absoluta
     - Frecuencia relativa
     - Frecuencia acumulada
   - Incluye opciones para ordenar los datos y mostrar los resultados en una tabla interactiva.

2. **Gráfica de Barras**
   - Permite generar una gráfica de barras a partir de dos conjuntos de datos: etiquetas (X) y valores (Y).
   - Proporciona controles para ingresar los datos y visualizar la gráfica generada en la interfaz.

3. **Gráfica de Pastel**
   - Crea una gráfica de pastel a partir de etiquetas y valores para mostrar la distribución porcentual de cada categoría.
   - Ideal para visualizar la composición de categorías dentro de un conjunto de datos.

4. **Gráfica de Serie de Tiempo**
   - Permite crear una gráfica de serie de tiempo con valores X e Y que representan el tiempo y el valor correspondiente en cada periodo.
   - La gráfica incluye un eje de tiempo y un eje de valor para facilitar el análisis temporal.

5. **Histogramas y Polígonos de Frecuencia**
   - Genera histogramas y polígonos de frecuencia a partir de datos agrupados.
   - Calcula intervalos de clase y frecuencias para representar visualmente la distribución de los datos.

#### Tema 3_4: Medidas de Tendencia Central, Dispersión y Posición

Este tema incluye cálculos avanzados de estadística descriptiva y medidas de dispersión para datos agrupados e individuales.

1. **Medidas de Tendencia Central**
   - Calcula:
     - **Media**: promedio de los datos.
     - **Mediana**: valor central de los datos.
     - **Moda**: valor o valores que aparecen con mayor frecuencia.
   - Funciona para datos agrupados e individuales, permitiendo elegir el tipo de datos en la interfaz.

2. **Medidas de Posición (Cuartiles, Deciles y Percentiles)**
   - Calcula cuartiles (Q1, Q2, Q3), deciles (1 al 9) y percentiles (1 al 99) para analizar la posición relativa de los datos.
   - Funciona con datos agrupados e individuales, facilitando el análisis estadístico profundo de la distribución de datos.

3. **Medidas de Dispersión**
   - Incluye el cálculo de:
     - **Varianza** (poblacional y muestral): mide la dispersión de los datos respecto a la media.
     - **Desviación Estándar** (poblacional y muestral): indica la variabilidad de los datos.
     - **Rango Intercuartil**: mide la dispersión en el rango medio de los datos, calculado entre el primer y tercer cuartil.
   - Estos cálculos están disponibles para datos agrupados e individuales.

4. **Coeficiente de Variación**
   - Calcula el coeficiente de variación, que es una medida relativa de dispersión que muestra la relación entre la desviación estándar y la media.
   - El resultado incluye una estimación de precisión:
     - Precisas (≤ 7%)
     - Aceptables (8-14%)
     - Regulares (15-20%)
     - Poco precisas (> 20%)

#### Tema 5_6: Espacio Muestral, Permutaciones y Combinaciones

Este tema facilita el cálculo y análisis de espacio muestral, unión e intersección de eventos, así como cálculos de permutaciones y combinaciones.

1. **Espacio Muestral y Eventos**
   - Permite ingresar el espacio muestral y calcular la unión, intersección y complemento de eventos.

2. **Permutaciones**
   - Permite calcular permutaciones con o sin repetición.

3. **Combinaciones**
   - Permite calcular combinaciones con o sin repetición.

#### Tema 7_8: Cálculo de Probabilidades y Reglas Básicas

Este tema abarca cálculos básicos de probabilidades y reglas para el análisis de eventos.

1. **Probabilidad de un Evento**
   - Calcula la probabilidad de un evento específico en un espacio muestral dado.

2. **Regla Aditiva**
   - Calcula la probabilidad de la unión de dos eventos no excluyentes.

3. **Probabilidad Condicional**
   - Permite calcular la probabilidad de un evento condicionado a otro.

4. **Eventos Independientes**
   - Calcula la probabilidad de eventos independientes.

5. **Regla del Producto**
   - Calcula la probabilidad de eventos conjuntos aplicando la regla multiplicativa.

#### Tema 10_11: Distribuciones de Probabilidad Discretas

Este tema permite calcular distribuciones de probabilidad discretas comunes.

1. **Distribución Binomial**
2. **Distribución Multinomial**
3. **Distribución Hipergeométrica**
4. **Distribución Geométrica**
5. **Distribución de Poisson**

Cada distribución cuenta con campos específicos para ingresar los parámetros necesarios y calcular la probabilidad correspondiente.

## Requisitos de Instalación

Asegúrate de tener Python y las bibliotecas necesarias instaladas:

```bash
pip install flet matplotlib
