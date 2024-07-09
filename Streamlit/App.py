import streamlit as st
import requests

# Configurar la página
st.set_page_config(
    page_title="Fecundidad en Sudamérica",
    page_icon="🌎",
    layout="wide"
)

# Estilo CSS para personalización adicional
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.unicef.org/mexico/sites/unicef.org.mexico/files/styles/hero_tablet/public/nof%20acebook%20MR_UNICEF_Yucat%C3%A1n_2012_0034%20%282%29.jpg.webp?itok=j8ecL54P");
    background-size: cover;
    background-position: center;
    color: white;  /* Color de texto predeterminado para todo el contenido */
}
[data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0.7);
}
h1, h2, h4, h5 {
    font-family: 'Arial', sans-serif;
    color: white;
}
p {
    font-family: 'Arial', sans-serif;
    color: white;
    text-align: justify;
}
</style>
'''

# Definir el estilo de la página
st.markdown(page_bg_img, unsafe_allow_html=True)

# Título y subtítulo centrado con fondo semi-transparente
st.markdown("""
    <div style='text-align: center; background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h1>Fecundidad en los países de Sudamérica</h1>
        <h4>Un análisis del comportamiento de las tasas</h4>
    </div>
""", unsafe_allow_html=True)

# Texto principal con espaciado y formato mejorado
st.markdown("""
    <div style='background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 10px;'>
        <p>La fecundidad puede interpretarse como la realización efectiva de la fertilidad, es decir, la reproducción biológica en cualquier especie. En el contexto humano, se refiere a la capacidad efectiva de una mujer de producir un nacimiento durante su vida fértil.</p>
        <p>Desde el siglo XX, la demografía mundial ha sufrido cambios significativos, y Sudamérica no ha sido ajena a estos. En tan solo tres décadas, la tasa de fecundidad ha disminuido casi a la mitad en varios países de la región, lo que tiene implicaciones demográficas, económicas y sociales.</p>
        <h5>Consecuencias a nivel demográfico:</h5>
        <ul>
            <li><strong>Envejecimiento de la población</strong>: Una baja tasa de fecundidad puede conducir a una población envejecida, con menos nacimientos y una mayor proporción de personas mayores.</li>
            <li><strong>Disminución de la población: Si la tasa de fecundidad cae por debajo del nivel de reemplazo (aproximadamente 2.1 hijos por mujer), la población total puede comenzar a disminuir a largo plazo.</li>
        </ul>
        <h5>Consecuencias a nivel económico:</h5>
        <ul>
            <li><strong>Reducción de la fuerza laboral</strong>: Una menor cantidad de nacimientos puede llevar a una reducción en el número de personas en edad laboral, afectando la productividad y el crecimiento económico.</li>
            <li><strong>Aumento de los costos de la seguridad social</strong>: Con una población envejecida, los costos de las pensiones y la atención médica aumentan, poniendo presión sobre los sistemas de seguridad social y los presupuestos gubernamentales.</li>
            <li><strong>Cambio en la demanda de bienes y servicios</strong>: Una población envejecida puede cambiar la demanda de ciertos bienes y servicios, afectando sectores económicos específicos (por ejemplo, mayor demanda de servicios de salud y menor demanda de educación infantil).</li>
        </ul>
        <h5>Consecuencias a nivel social:</h5>
        <ul>
            <li><strong>Cambio en las estructuras familiares</strong>: Las familias más pequeñas pueden afectar la dinámica familiar, con menos hermanos y una mayor carga de cuidado para los hijos hacia los padres ancianos.</li>
            <li><strong>Impacto en la educación y desarrollo infantil</strong>: La inversión en educación y desarrollo infantil podría aumentar debido a una mayor disponibilidad de recursos por niño, pero también podría haber menos escuelas y recursos educativos disponibles a medida que disminuye la población infantil.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Cargar gráfico de las tasas de fecundidad de todos los países
fig = 'https://raw.githubusercontent.com/JuankTS/Fecuendidad-en-America-Latina-/main/Images/Fecundidad_sudanerica.html'
response = requests.get(fig)
if response.status_code == 200:
    html_content = response.text  # Obtener el contenido HTML como texto
    st.components.v1.html(html_content, height=800)
else:
    st.error(f"Error al descargar el archivo HTML desde {fig}. Status code: {response.status_code}")

st.markdown("""
    <div style='background-color: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 10px;'>
        <p>Ahora bien, teniendo en cuenta las consecuencias y el gráfico que nos muestra el comportamiento de las tasas de fecundidad en Sudamérica, la pregunta que nos queda ahora es: ¿Qué ha pasado? ¿Por qué las tasas han descendido?</p>
        <p>El grupo de once variables propuesto por Davis and Blake en 1956 fue trabajado por varios investigadores, entre ellos J. Bongaarts (1978, 1982), quien demostró que la fecundidad de las poblaciones se debe, mayormente, a la variación en por lo menos una de cuatro de ellas:</p>
        <ul>
            <li><strong>Nupcialidad</strong>: Los factores relacionados con la nupcialidad que afectan la fecundidad son el porcentaje de mujeres que se unen y su contraparte, el porcentaje de mujeres que permanecen solteras, la edad de la primera unión y la estabilidad de las uniones. En la mayoría de las culturas del mundo, el matrimonio formal o consensual tiene como finalidad la formación de una familia, lo que nos lleva a pensar en la reproducción. Sin embargo, la nupcialidad se ha visto afectada por factores como la inserción de la mujer en el mercado laboral y nuevas ideologías de género, entre otros. Estos factores han contribuido a la modificación del patrón de comportamiento y el contexto cultural de nuestras sociedades, lo que ha llevado a una evidente disminución en la nupcialidad.</li>
            <li><strong>Uso de anticonceptivos</strong>: La mayoría de la literatura sobre la transición de altos a bajos niveles de fecundidad en la región abunda en evidencia en el sentido de que esta ocurrió predominantemente por el incremento en el uso de anticonceptivos.</li>
            <li><strong>Infecundidad posparto</strong>: Después del parto y antes del retorno de la menstruación, el riesgo de concebir es prácticamente inexistente y depende, en gran parte, de la duración e intensidad de la lactancia, que, como se sabe, produce amenorrea (la supresión biológica de la menstruación) y, en consecuencia, la postergación del regreso de la fertilidad. También factores como la abstinencia sexual o procedimientos quirúrgicos como la ligadura de trompas contribuyen a este factor.</li>
            <li><strong>El aborto inducido</strong>: El aborto ha sido un tema controvertido en distintos países. Esto también depende mucho del contexto cultural, pero sin lugar a dudas, la normalización y legalización del aborto ha contribuido a que las tasas de fecundidad tiendan a ser más bajas. Esto se debe en parte a que las mujeres tienen más opciones para evitar nacimientos no deseados o embarazos de alto riesgo, lo que también puede influir en las decisiones de tener hijos y en la tasa de fecundidad general.</li>
        </ul>
        <p>Otro factor que normalmente no se suele mencionar es el <strong>aumento del costo de vida</strong>. Los altos niveles en los costos de vida actualmente llevan a las mujeres y parejas a repensar el hecho de tener un hijo, ya que este conlleva un gran costo de oportunidad a nivel económico junto con una gran demanda de tiempo. Esta puede ser otra variable que se una a las determinantes de la baja tasa de fecundidad que estamos experimentando en la actualidad.</p>
    </div>
    """, unsafe_allow_html=True)
# Seleccionar pronóstico por país
st.markdown("<h2 style='text-align: center; color: white;'>Pronóstico por país</h2>", unsafe_allow_html=True)
countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela', 'Sudamérica']
pais = st.selectbox(label="Selecciona un país:", options=countries)

image = f'https://raw.githubusercontent.com/JuankTS/Fecuendidad-en-America-Latina-/main/Images/forecast_{pais}.html'
resp = requests.get(image)
if resp.status_code == 200:
    html_content = resp.text  # Obtener el contenido HTML como texto
    st.components.v1.html(html_content, height=800)
else:
    st.error(f"Error al descargar el archivo HTML desde {image}. Status code: {resp.status_code}")
