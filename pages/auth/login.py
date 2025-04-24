import streamlit as st
from utils.auth import login_user

st.title("Aplicación PETI")
st.subheader("Iniciar Sesión")
email = st.text_input("Correo electrónico")
passwd = st.text_input("Contraseña", type="password")
if st.button("Ingresar"):
    user = login_user(email, passwd)
    if user:
        st.session_state.logged_in = True
        st.session_state.user_name = user.username
        st.success("Ingreso exitoso")
        st.rerun()
    else:
        st.error("Correo o contraseña incorrectos")
