<h1 align='center'>Fecundidad en América del Sur 🌎</h1>

<img align='center' src='https://www.unicef.org/mexico/sites/unicef.org.mexico/files/styles/hero_tablet/public/nof%20acebook%20MR_UNICEF_Yucat%C3%A1n_2012_0034%20%282%29.jpg.webp?itok=j8ecL54P'>
<br>

Las condiciones mundiales en las que vivimos han experimentado cambios significativos desde el siglo pasado, cambios a los que Sudamérica no ha sido ajena y que se han reflejado en los distintos aspectos de nuestra población. Cambios en los aspectos económicos, en nuestro contexto social y cultural, han tenido afectaciones en nuestras variables demográficas. Una de las más importantes para una población es la tasa de fecundidad, la cual se ha visto afectada por toda esta trascendencia, mostrando una reducción de casi el doble en las últimas 4 décadas. Esto trae ciertos acontecimientos que se deben considerar. Por eso, en este proyecto se dedica a hacer un análisis de las tasas de fecundidad en Sudamérica y las repercusiones y efectos sobre nuestra población.

<h2>
    Datos y su procesamiento
    <img src="https://media.giphy.com/media/MF3pE1wwVczhKkaSlg/giphy.gif"  width="70" height="70">
</h2>

Para este proyecto se usaron datos del [Banco Mundial](https://data.worldbank.org/indicator/SP.DYN.TFRT.IN) sobre el reporte de las tasas de fecundidad, las cuales fueron extraídas de los países de América del Sur. 
Los datos incluyen información detallada sobre el número promedio de hijos por mujer en diferentes países y en varios años, permitiendo así un análisis longitudinal y comparativo.

Los datos fueron procesados utilizando la biblioteca pandas de Python, que facilitó la limpieza, manipulación y análisis de los mismos.

Posteriormente, las visualizaciones se realizaron con plotly, una biblioteca interactiva que permitió crear gráficos dinámicos y visualmente atractivos. Estos gráficos comparaciones entre países y proyecciones futuras, proporcionando una visión clara y detallada de cómo ha evolucionado la tasa de fecundidad en la región y qué podemos esperar en el futuro.

<h2>
    Aplicativo en Streamlit
    <img src="https://media.giphy.com/media/IUNycHoVqvLDowiiam/giphy.gif"  width="70" height="70">
</h2>

<p align='center'>
    <a href='https://fecunidadsudamerica.streamlit.app/'>
    <img src='Images/FecundidadGif.gif' width="800" height="400">
    </a>
</p>

Se usó Streamlit para desarrollar un aplicativo web [(ver código)](https://github.com/JuankTS/Fecuendidad-en-America-Latina-/blob/main/Streamlit/App.py) donde se concentra la información y puede ser disponible para todo observador. En el aplicativo web podrás explorar datos, visualizaciones y predicciones sobre las tasas de fecundidad en diferentes países de América del Sur. Las predicciones se realizaron usando un modelo de suavización exponencial con tendencia aditiva [(Más información)](https://www.ibm.com/docs/es/spss-statistics/saas?topic=modeler-custom-exponential-smoothing-models) para crear pronósticos del comportamiento de la tasa de fecundidad en los diferentes países de la región para los próximos años. Junto a esto, también encontrarás un análisis desde los distintos aspectos de una población. Podrás ver el aplicativo dando clic [aquí](https://fecunidadsudamerica.streamlit.app/) o tocando el gif.

<h2>
    Referencias
    <img src="https://media.giphy.com/media/XFvr8JBCeMF6X496LF/giphy.gif"  width="70" height="70">
</h2>

- [CEPAL - Análisis de fecundidad](https://repositorio.cepal.org/server/api/core/bitstreams/c3e805c8-54ec-4857-bec0-2acf77002dbb/content)
- [DANE - Fecundidad en Colombia](https://geoportal.dane.gov.co/servicios/atlas-estadistico/src/Tomo_I_Demografico/4.1.-fecundidad.html)

<div align="center">
  <a href='https://www.linkedin.com/in/juan-camilo-torres-salas-907749265/'><img src="https://skillicons.dev/icons?i=linkedin"/></a>
  <a href="mailto:torressalasjc@gmail.com"><img src="https://skillicons.dev/icons?i=gmail&theme=light" alt="Gmail"/></a>
</div>
