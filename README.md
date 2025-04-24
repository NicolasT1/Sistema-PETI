# 🧠 Aplicación PETI - Plan Estratégico de Tecnologías de Información

Esta aplicación permite registrar, iniciar sesión y acceder a un dashboard donde se podrá construir paso a paso un Plan Estratégico de Tecnologías de Información (PETI).

Funciona 100% en local usando Python, Streamlit y PostgreSQL.

---

## ⚙️ Requisitos

- Python 3.8 o superior
- PostgreSQL instalado localmente
- pip para instalar dependencias

---

## 📦 Instalación

1. **Clona este repositorio:**
```bash
git clone https://github.com/tuusuario/peti-app.git
cd peti-app
```
Crea y activa un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```
Instala las dependencias:

```bash
pip install -r requirements.txt
```
Configura tu base de datos PostgreSQL:

Asegúrate de tener PostgreSQL corriendo y ejecuta:

```sql
CREATE DATABASE peti_db;

\c peti_db

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);
```
Importante: Cambia los datos de conexión en database.py según tu usuario, contraseña y host.

```python
DATABASE_URL = "postgresql://user:password@localhost/peti_db"
```

🚀 Ejecución
Corre el archivo principal con Streamlit:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en http://localhost:8501

📁 Estructura del proyecto
```bash
peti-app/
│
├── app.py            # Interfaz principal Streamlit
├── auth.py           # Lógica de login y registro
├── database.py       # Conexión y modelo de base de datos
├── requirements.txt  # Librerías necesarias
├── README.md         # Esta guía
└── .gitignore        # Archivos a excluir del control de versiones
```

✅ Pendiente
Agregar navegación por módulos del PETI

Exportar plan a PDF/Excel

Mejorar diseño visual del dashboard