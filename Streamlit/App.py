import streamlit as st
import requests

# Configurar la página
st.set_page_config(
    page_title="Fecundidad en Sudamérica",
    page_icon="🌐",  
)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.unicef.org/mexico/sites/unicef.org.mexico/files/styles/hero_tablet/public/nof%20acebook%20MR_UNICEF_Yucat%C3%A1n_2012_0034%20%282%29.jpg.webp?itok=j8ecL54P");
    background-size: cover;
    background-position: center;
    color: white;  /* Color de texto predeterminado para todo el contenido */
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Cargar grafico de las tasas de fecundidad  de todos los paises
fig = 'https://raw.githubusercontent.com/JuankTS/Fecuendidad-en-America-Latina-/main/Images/Fecundidad_sudanerica.html'

# Descargar el contenido HTML
response = requests.get(fig)

# Verificar si la descarga fue exitosa
if response.status_code == 200:
    html_content = response.text  # Obtener el contenido HTML como texto
    st.components.v1.html(html_content, height=800)
else:
    st.error(f"Error al descargar el archivo HTML desde {fig}. Status code: {response.status_code}")

# Seleccionar pronostico por país
countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 
        'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela' ,'Sudamérica']

pais = st.selectbox(label="Selecciona un país:",options=countries)


image=f'https://raw.githubusercontent.com/JuankTS/Fecuendidad-en-America-Latina-/main/Images/forecast_{pais}.html'
resp = requests.get(image)
if resp.status_code == 200:
    html_content = resp.text  # Obtener el contenido HTML como texto
    st.components.v1.html(html_content, height=800)
else:
    st.error(f"Error al descargar el archivo HTML desde {image}. Status code: {response.status_code}")