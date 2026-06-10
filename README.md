PEC4 – LaLiga Data Science Project
Proyecto de la asignatura Programación para la Ciencia de Datos (UOC).
El objetivo es analizar datos históricos de La Liga (1995–2025) mediante Python, aplicando técnicas de análisis, visualización, modelado y grafos.

El proyecto está completamente modularizado y se ejecuta mediante argumentos desde main.py.

📁 Contenido del repositorio
Código
PEC4-LaLiga-DataScience/
│
├── src/
│   ├── main.py
│   └── exercises/
│       ├── ex1.py
│       ├── ex2.py
│       ├── ex3.py
│       ├── ex4.py
│       ├── ex5.py
│       ├── ex6.py
│       └── ex7.py
│
├── data/
│   └── LaLiga_Matches.csv
│
├── img/
│   └── (gráficas generadas automáticamente)
│
├── tests/
├── doc/
├── screenshots/
│
├── config.py
├── requirements.txt
├── LICENSE
└── README.md
⚙️ Requisitos
Instalar dependencias:

Código
pip install -r requirements.txt
Librerías principales:

pandas

numpy

matplotlib

seaborn

scikit-learn

networkx

▶️ Ejecución
Cada ejercicio se ejecuta desde main.py usando el argumento -ex:

Código
python src/main.py -ex 1
python src/main.py -ex 2
...
python src/main.py -ex 7
Las gráficas se guardan automáticamente en la carpeta img/.

📊 Descripción de los ejercicios
Ejercicio 1
Carga del dataset y visualización de goles locales vs visitantes.

Ejercicio 2
Cálculo de estadísticas de goles y creación de un histograma de goles totales.

Ejercicio 3
Cálculo de partidos jugados, victorias, empates y derrotas por equipo.
Gráfico de barras de victorias.

Ejercicio 4
Goles por temporada (locales y visitantes).
Gráfico de líneas.

Ejercicio 5
Cálculo de matriz de correlación y heatmap.

Ejercicio 6
Modelo de regresión lineal para predecir goles totales.
Gráfico de valores reales vs predichos.

Ejercicio 7
Cálculo de los 5 equipos con más puntos acumulados.
Generación de un grafo de conexiones entre ellos usando NetworkX.

👤 Autor
Xaime Ferrín  
Universitat Oberta de Catalunya (UOC)

📄 Licencia
Este proyecto está bajo licencia MIT.
