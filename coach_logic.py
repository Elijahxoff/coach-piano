import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_session(niveau, duree, ambiance):
    prompt = (
        f"Crée une session d'entraînement de piano pour un niveau {niveau}, "
        f"d'une durée de {duree} minutes, avec une ambiance {ambiance}. "
        "Fais en sorte que cela aide à devenir compositeur de musique de film."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "gpt-4" si tu as accès
        messages=[
            {"role": "system", "content": "Tu es un coach de piano spécialisé en musique de film."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
