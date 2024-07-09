import streamlit as st
import requests

# Configurar la página
st.set_page_config(
    page_title="Fecundidad en Sudamérica",
    page_icon="🌐",
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
h1, h4 , h5{
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
    <div style='text-align: center; background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h1>Fecundidad en los países de Sudamérica</h1>
        <h4>Un análisis del comportamiento de las tasas</h4>
    </div>
""", unsafe_allow_html=True)

# Texto principal con espaciado y formato mejorado
st.markdown("""
    <div style='background-color: rgba(0, 0, 0, 0.5); padding: 20px; border-radius: 10px;'>
        <p>La fecundidad puede interpretarse como la realización efectiva de la fertilidad, es decir, la reproducción biológica en cualquier especie. En el contexto humano, se refiere a la capacidad efectiva de una mujer de producir un nacimiento durante su vida fértil.</p>
        <p>Desde el siglo XX, la demografía mundial ha sufrido cambios significativos, y Sudamérica no ha sido ajena a estos. En tan solo tres décadas, la tasa de fecundidad ha disminuido casi a la mitad en varios países de la región, lo que tiene implicaciones demográficas, económicas y sociales.</p>
        <h5>Consecuencias a nivel demográfico:</h5>
        <ul>
            <li>Envejecimiento de la población: Una baja tasa de fecundidad puede conducir a una población envejecida, con menos nacimientos y una mayor proporción de personas mayores.</li>
            <li>Disminución de la población: Si la tasa de fecundidad cae por debajo del nivel de reemplazo (aproximadamente 2.1 hijos por mujer), la población total puede comenzar a disminuir a largo plazo.</li>
        </ul>
        <h5>Consecuencias a nivel económico:</h5>
        <ul>
            <li>Reducción de la fuerza laboral: Una menor cantidad de nacimientos puede llevar a una reducción en el número de personas en edad laboral, afectando la productividad y el crecimiento económico.</li>
            <li>Aumento de los costos de la seguridad social: Con una población envejecida, los costos de las pensiones y la atención médica aumentan, poniendo presión sobre los sistemas de seguridad social y los presupuestos gubernamentales.</li>
            <li>Cambio en la demanda de bienes y servicios: Una población envejecida puede cambiar la demanda de ciertos bienes y servicios, afectando sectores económicos específicos (por ejemplo, mayor demanda de servicios de salud y menor demanda de educación infantil).</li>
        </ul>
        <h5>Consecuencias a nivel social:</h5>
        <ul>
            <li>Cambio en las estructuras familiares: Las familias más pequeñas pueden afectar la dinámica familiar, con menos hermanos y una mayor carga de cuidado para los hijos hacia los padres ancianos.</li>
            <li>Impacto en la educación y desarrollo infantil: La inversión en educación y desarrollo infantil podría aumentar debido a una mayor disponibilidad de recursos por niño, pero también podría haber menos escuelas y recursos educativos disponibles a medida que disminuye la población infantil.</li>
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
