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
# URL directa al archivo HTML en GitHub (en formato raw)
file_url = 'https://raw.githubusercontent.com/JuankTS/Fecuendidad-en-America-Latina-/b19b5f4173eacc0807ba17f31b25a27e1eff2f91/Images/Fecundidad_sudanerica.html'

# Mostrar el gráfico en Streamlit desde la URL
st.components.v1.html(file_url, height=800)

# Seleccionar pronostico por país
countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 
        'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela' ,'Sudamérica']

pais = st.selectbox(label="Selecciona un país:",options=countries)

if st.button('Mostrar'):
    image=f'https://raw.githubusercontent.com/JuankTS/Fecuendidad-en-America-Latina-/b19b5f4173eacc0807ba17f31b25a27e1eff2f91/Images/Fecundidad_{pais}.html'
    st.components.v1.html(image, height=800)