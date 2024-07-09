import streamlit as st

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
with open('../Images/Fecundidad_sudanerica.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    
st.components.v1.html(html_content, height=800)

# Seleccionar pronostico por país
countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 
        'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela' ,'Sudamérica']

pais = st.selectbox(label="Selecciona un país:",options=countries)

if st.button('Mostrar'):
    with open(f'../Images/forecast_{pais}.html', 'r', encoding='utf-8') as file:
        forecast_html = file.read()
    st.components.v1.html(forecast_html, height=800)