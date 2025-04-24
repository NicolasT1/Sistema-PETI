import streamlit as st

st.title("Resumen del Formulario")

st.write("### Sección 0 - Información de la Empresa")
st.write(f"Nombre de la empresa: {st.session_state.form_0['nombre_empresa']}")
st.write(f"Descripción: {st.session_state.form_0['descripcion_empresa']}")

# Mostrar el logo si fue subido
logo = st.session_state.form_0["logo_empresa"]
if logo:
    st.image(logo, caption="Logo de la empresa", width=200)

st.write("### Sección 1 - Misión")
st.write(st.session_state.form_1["mision"])

st.write("### Sección 2 - Visión")
st.write(st.session_state.form_2["vision"])

st.write("### Sección 3 - Valores")
valores = st.session_state.form_3["valores"]
for i, valor in enumerate(valores):
    if valor:
        st.write(valor)
