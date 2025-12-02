from google import genai
import json
import re


def set_prompt(text):
    """Generate the prompt and return it as json."""


    prompt = f"""
        Erstellen Sie anhand des folgenden Transkripts ein Quiz im gültigen JSON-Format. Entferne alle sonderzeichen wie ``` und json. 


        Das Quiz muss folgende Struktur aufweisen:
        {{
            "title": "Geben Sie einen prägnanten Quiztitel basierend auf dem Thema des Transkripts.",
            "description": "Fassen Sie das Transkript in maximal 300 Zeichen zusammen. Fügen Sie keine Quizfragen oder -antworten hinzu.",
            "questions": [
                {{
                    "question_title": "Hier kommt die Frage hin.",
                    "question_options": ["Option A", "Option B", "Option C", "Option D"],
                    "answer": "Die richtige Antwort aus den obigen Optionen."
                }},
                ...
                (genau 10 Fragen)
            ]
        }}
        Anforderungen:
            - Jede Frage muss genau 4 verschiedene Antwortmöglichkeiten haben.
            - Pro Frage ist nur eine richtige Antwort zulässig, und diese muss in 'question_options' enthalten sein.
            - Die Ausgabe muss gültiges JSON sein und direkt geparst werden können (z. B. mit der Python-Funktion `json.loads`).
            - Fügen keine Erklärungen, Kommentare oder sonstigen Text außerhalb des JSON-Formats ein.

            
        Transkript:
        {text}
    """
    client = genai.Client()
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    json = clean_json_string(response.text)
    return json


def clean_json_string(json_string):
    """Clean the json from special characters."""


    edit_json_string = re.sub(r'(?i)json', '', json_string)
    edit_json_string = re.sub(r'```', '', json_string)
    return json.loads(edit_json_string)    