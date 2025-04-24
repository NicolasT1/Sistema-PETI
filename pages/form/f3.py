import streamlit as st

# Función para la Sección 3 - Valores
st.subheader("Sección 3 - Valores")
st.markdown(
    """
        Los *VALORES* de una empresa son el conjunto de principios, reglas y aspectos culturales con los que se rige la organización. Son las pautas de comportamiento de la empresa y generalmente son pocos, entre 3 y 6. Son tan fundamentales y tan arraigados que casi nunca cambian.
        
        Ejemplo de valores:
        - Integridad
        - Compromiso con el desarrollo humano.			
        - Ética profesional
        - Responsabilidad social. 					
        - Innovación 		
        - Etc.
    """
)
# Mostrar los valores actuales
for i, valor in enumerate(st.session_state.form_3["valores"]):
    st.session_state.form_3["valores"][i] = st.text_input(f"Valor {i+1}", value=valor)

# Botón para añadir un nuevo campo de valor
if st.button("Añadir valor"):
    st.session_state.form_3["valores"].append("")
