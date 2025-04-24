import streamlit as st

# Función para la Sección 1 - Misión
st.subheader("Sección 1 - Misión")
st.markdown(
    """
        La *MISIÓN* es la razón de ser de la empresa/organización.
                                                    
        - Debe ser clara, concisa y compartida. 
        - Siempre orientada hacia el cliente no hacia el producto o servicio. 
        - Refleja el propósito fundamental de la empresa en el mercado.

        En términos generales describe la actividad y razón de ser de la organización y contribuye como una referencia permanente en el proceso de planificación estratégica.
        Se expresa a través de una oración que define el propósito fundamental de su existencia, estableciendo qué hace la empresa, por qué y para quién lo hace, 
    """
)
mision = st.text_area("Misión de la empresa", value=st.session_state.form_1["mision"])

st.session_state.form_1["mision"] = mision


def click_button():
    st.session_state.form_1["mision"] = mision
    st.success("Información guardada correctamente.")


st.button("Guardar información", on_click=click_button)
