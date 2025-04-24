import streamlit as st
from utils.auth import register_user

st.subheader("Crear Cuenta")
user = st.text_input("Nombre de usuario")
email = st.text_input("Correo electrónico")
passwd = st.text_input("Contraseña", type="password")
passwd2 = st.text_input("Repetir contraseña", type="password")

if st.button("Registrar"):
    if passwd != passwd2:
        st.warning("Las contraseñas no coinciden")
    elif len(passwd) < 6:
        st.warning("La contraseña debe tener al menos 6 caracteres")
    else:
        try:
            register_user(user, passwd, email)
            st.success("Usuario registrado correctamente")
        except:
            st.error(
                "Error al registrar. Verifica que el correo o usuario no estén en uso."
            )
