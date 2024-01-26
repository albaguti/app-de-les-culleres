import streamlit as st
import datetime
import locale
from save_info_db import save_data

try:
   # Set the locale to Catalan
   locale.setlocale(locale.LC_TIME, 'ca_ES.UTF-8')
except locale.Error:
   print("Locale not found.")

st.set_page_config(
   page_title="App de les culleres",
   page_icon="culleres.ico",
)


st.header("App de les culleres", divider='rainbow')
avui = datetime.datetime.now()
avui_format = avui.strftime("%A, %d de %B de %Y")
st.markdown(f"### :rainbow[Avui és: {avui_format}]")
st.divider()

# Qualitat del son
st.markdown('### <u>Com has dormit?</u>', unsafe_allow_html=True)

hores_de_son = st.slider("Quantes hores has dormit?", min_value=0.0, max_value=10.0, step= 0.5)

qualitat = st.select_slider("Has descansat", ("Gens", "Molt poc","Poc", "Normal", "Bé", "Molt bé"))

despertat = st.slider("Quantes vegades t'has despertat?", min_value=0, max_value=4)

st.divider()

# Activitats durant el dia
st.markdown('### <u>Que tal ha anat el dia?</u>', unsafe_allow_html=True )

hores_treballades = st.slider('Quantes hores has treballat?', min_value=0.0, max_value=12.0, step=0.2)

cites = st.selectbox('Quantes cites has tingut avui?', [0,1,2,3,4,5])

nens = st.radio('Has tingut els nens avui?', ('Si', 'No'))

benestar = st.multiselect("Que has fet per trobar-te millor?", ("Res", "Banyar-me", "Esport", "Passejar", "Comprar", "Hobbies"))
st.divider()

# Estat general al final del dia
st.markdown('### <u>Com estàs?</u>', unsafe_allow_html=True)

estat = st.select_slider('Selecciona com et trobes', ("Fatal", "Malament","Cansada","Necessito dormir", "Ni bé ni malamnet", "Bé", "Podria fer més", "Molt bé" ))

# Resum general
st.header("Resum del dia", divider='rainbow')

st.markdown(f":clock930: **Hores dormides:** {hores_de_son}")

st.markdown(f":bed: **Qualitat del son:** {qualitat}")

st.markdown(f":office_worker: **Hores treballades:** {hores_treballades}")

st.markdown(f":rage: **Hores cites:** {cites}")

st.markdown(f":woman-girl-girl: **Nens?** {nens}")
st.markdown(f":massage: **Que has fet per trobar-te millor?** {benestar}")
st.markdown(f'**Així doncs en general et trobes:** {estat}')

if st.button("Salva els resultats"):
    save_data(avui, hores_treballades, cites, nens, hores_de_son, qualitat, estat, despertat, benestar )
