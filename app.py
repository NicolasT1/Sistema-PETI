import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.form_0 = {
        "nombre_empresa": "",
        "descripcion_empresa": "",
        "logo_empresa": None,
    }
    st.session_state.form_1 = {
        "mision": "",
    }
    st.session_state.form_2 = {
        "vision": "",
    }
    st.session_state.form_3 = {"valores": ["", "", "", "", ""]}

login_page = st.Page(
    "pages/auth/login.py", title="Iniciar Sesión", icon=":material/login:"
)
register_page = st.Page(
    "pages/auth/register.py", title="Registrar Usuario", icon=":material/history:"
)
logout_page = st.Page(
    "pages/auth/logout.py", title="Cerrar Sesión", icon=":material/logout:"
)

dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/home:")

f0 = st.Page(
    "pages/form/f0.py",
    title="Información de la Empresa",
    icon=":material/home:",
)
f1 = st.Page(
    "pages/form/f1.py",
    title="Misión",
    icon=":material/home:",
)
f2 = st.Page(
    "pages/form/f2.py",
    title="Visión",
    icon=":material/home:",
)
f3 = st.Page(
    "pages/form/f3.py",
    title="Valores",
    icon=":material/home:",
)
resumen = st.Page(
    "pages/resumen.py",
    title="Resumen",
    icon=":material/home:",
)

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Principal": [dashboard, logout_page],
            "Formularios": [f0, f1, f2, f3],
            "Resultados": [resumen],
        }
    )
else:
    pg = st.navigation({"Ingresa": [login_page, register_page]})

pg.run()
