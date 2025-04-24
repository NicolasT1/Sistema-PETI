import streamlit as st

# Función para la Sección 2 - Visión
st.subheader("Sección 2 - Visión")
st.markdown(
    """
        La *VISION* de una empresa define lo que la empresa/organización quiere lograr en el futuro. Es lo que la organización aspira llegar a ser en torno a  2 -3 años. 

        - Debe ser retadora, positiva, compartida y coherente con la misión. 
        - Marca el fin último que la estrategia debe seguir. 
        - Proyecta la imagen de destino que se pretende alcanzar.
        
        La visión debe ser conocida y compartida por todos los miembros de la empresa y también por aquellos que se relacionan con ella.
    """
)
vision = st.text_area("Visión de la empresa", value=st.session_state.form_2["vision"])
st.session_state.form_2["vision"] = vision


def click_button():
    st.session_state.form_2["vision"] = vision
    st.success("Información guardada correctamente.")


st.button("Guardar información", on_click=click_button)
