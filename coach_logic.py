import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_session(level, duration, ambiance):
    prompt = (
        f"Tu es un coach pour apprendre le piano, spécialisé en musique de film.\n"
        f"Niveau : {level}\n"
        f"Durée de la session : {duration} minutes\n"
        f"Ambiance souhaitée : {ambiance}\n"
        f"Propose une session adaptée, avec exercices et conseils."
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7,
    )

    return response.choices[0].message.content
