import openai
import streamlit as st
from prompts import session_prompt

openai.api_key = st.secret[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]
def generate_session(level, duration, ambiance):
    prompt = session_prompt.format(level=level, duration=duration, ambiance=ambiance)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )
    content = response["choices"][0]["message"]["content"]

    parts = content.split("###")
    return {
        "plan": parts[1].strip() if len(parts) > 1 else content,
        "exercices": parts[2].strip() if len(parts) > 2 else "",
        "suggestion_passive": parts[3].strip() if len(parts) > 3 else "",
    }
