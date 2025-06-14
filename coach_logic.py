import openai
import streamlit as st
from prompts import session_prompt

openai.api_key =  st.secrets["OPENAI_API_KEY"]
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
