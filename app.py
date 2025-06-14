import streamlit as st
from coach_logic import generate_session

st.set_page_config(page_title="Coach Piano Cinéma 🎹", layout="centered")

st.title("🎬 Coach Piano Cinéma")
st.markdown("Crée ta séance de piano personnalisée inspirée de la musique de film.")

level = st.selectbox("Ton niveau 🎼", ["Débutant", "Intermédiaire", "Avancé"])
duration = st.slider("Durée de la session (minutes) ⏱️", 10, 60, 20, 5)
ambiance = st.selectbox("Ambiance souhaitée 🎭", ["Nostalgique", "Épique", "Mélancolique", "Mystérieux", "Apaisant"])

if st.button("🎹 Générer ma session"):
    session = generate_session(level, duration, ambiance)
    st.markdown("### 🎯 Plan de session")
    st.write(session["plan"])

    st.markdown("### 🎶 Exercices & contenu")
    st.write(session["exercices"])

    st.markdown("### 🎧 Suggestion passive")
    st.write(session["suggestion_passive"])