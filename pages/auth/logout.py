import streamlit as st

st.title("Aplicación PETI")
st.title("Cerrar Sesión")
st.subheader("¿Está seguro de que desea cerrar sesión?")
if st.button("Cerrar sesión"):
    st.session_state.logged_in = False
    st.session_state.user_name = None
    st.success("Sesión cerrada correctamente")
    st.rerun()
