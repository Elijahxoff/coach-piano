import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_session(niveau, duree, ambiance):
    prompt = (
        f"Crée une session de piano pour un niveau {niveau}, "
        f"d'une durée de {duree} minutes, avec une ambiance {ambiance}. "
        "Propose des exercices ou idées adaptés à l’objectif de devenir compositeur de musique de film."
    )
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )

    return response.choices[0].text.strip()
