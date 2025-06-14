session_prompt = """
Tu es un coach de piano spécialisé dans la musique de film.
Crée une session personnalisée pour un·e pianiste de niveau {level}, qui dispose de {duration} minutes aujourd'hui.

L’ambiance musicale souhaitée est : {ambiance}.

Fournis :
### Plan de session
(avec timing approximatif)

### Exercices
(gammes, accords, rythme, travail d’un thème simple ou idée d’impro)

### Suggestion passive
(écoute, réflexion, analyse)
"""