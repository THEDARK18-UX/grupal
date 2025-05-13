import streamlit as st
import re

# Configuración de la página
st.set_page_config(page_title="⚗️ Estequiometría Simple", layout="centered")
st.title("⚗️ Calculadora Estequiométrica Interactiva")

# Masas molares simples
masas_molares = {
    "H": 1.008, "O": 16.00, "C": 12.01, "N": 14.01,
    "Cl": 35.45, "Na": 22.99, "K": 39.10, "Mg": 24.31,
    "Ca": 40.08, "S": 32.07, "Fe": 55.85, "Zn": 65.38
}

# Función para calcular masa molar desde fórmula como H2O o CO2
def calcular_masa_molar(formula):
    elementos = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    masa_total = 0
    for el, num in elementos:
        num = int(num) if num else 1
        masa_total += masas_molares.get(el, 0) * num
    return masa_total

# Paso 1: Selección de sustancias
st.subheader("Paso 1: Selecciona dos sustancias")
elementos = list(masas_molares.keys())

col1, col2 = st.columns(2)
with col1:
    elemento1 = st.radio("Sustancia conocida:", elementos)
with col2:
    elemento2 = st.radio("Sustancia a calcular:", [e for e in elementos if e != elemento1])

# Subíndices de las sustancias
col3, col4 = st.columns(2)
with col3:
    sub1 = st.slider(f"Subíndice de {elemento1}:", 1, 6, 1)
with col4:
    sub2 = st.slider(f"Subíndice de {elemento2}:", 1, 6, 1)

# Coeficientes balanceados
st.subheader("Paso 2: Ajusta los coeficientes balanceados")
col5, col6 = st.columns(2)
with col5:
    coef1 = st.slider(f"Coeficiente de {elemento1}{sub1 if sub1 > 1 else ''}:", 1, 10, 1)
with col6:
    coef2 = st.slider(f"Coeficiente de {elemento2}{sub2 if sub2 > 1 else ''}:", 1, 10, 1)

# Paso 3: Ingreso de gramos conocidos
st.subheader("Paso 3: Ingresa los gramos de la sustancia conocida")
gramos_conocidos = st.number_input(f"Gramos de {elemento1}{sub1 if sub1 > 1 else ''}:", min_value=0.0, step=0.1)

# Botón de cálculo
if st.button("📊 Calcular"):
    formula1 = f"{elemento1}{sub1 if sub1 > 1 else ''}"
    formula2 = f"{elemento2}{sub2 if sub2 > 1 else ''}"

    masa1 = calcular_masa_molar(formula1)
    masa2 = calcular_masa_molar(formula2)

    moles1 = gramos_conocidos / masa1
    proporcion = coef2 / coef1
    moles2 = moles1 * proporcion
    gramos2 = moles2 * masa2

    st.success(f"🔬 Resultado:\n\n"
               f"- Moles de {formula1}: {moles1:.4f} mol\n"
               f"- Gramos de {formula2} producidos: **{gramos2:.2f} g**")
