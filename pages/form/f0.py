import streamlit as st

# Función para la Sección 0 - Información de la Empresa
st.subheader("Sección 0 - Información de la Empresa")
st.markdown(
    """
        El Plan Estratégico de Tecnologías de la Información *PETI*, busca que la Entidad administre de manera eficiente los recursos de tecnología, los sistemas de información y la información, necesarios para la gestión de la organización.
    """
)

# Campos para nombre de la empresa, descripción y logo
nombre_empresa = st.text_input(
    "Nombre de la empresa", value=st.session_state.form_0["nombre_empresa"]
)
descripcion_empresa = st.text_area(
    "Descripción de la empresa", value=st.session_state.form_0["descripcion_empresa"]
)
logo_empresa = st.session_state.form_0["logo_empresa"]
logo_empresa = st.file_uploader(
    "Cargar logo de la empresa", type=["jpg", "png", "jpeg"]
)

if st.session_state.form_0["logo_empresa"]:
    st.image(
        st.session_state.form_0["logo_empresa"],
        caption="Logo de la empresa",
        width=200,
    )


def click_button():
    st.session_state.form_0["nombre_empresa"] = nombre_empresa
    st.session_state.form_0["descripcion_empresa"] = descripcion_empresa
    st.session_state.form_0["logo_empresa"] = logo_empresa
    st.success("Información guardada correctamente.")


st.button("Guardar información", on_click=click_button)
