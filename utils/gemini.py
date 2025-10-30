from google import genai


def set_prompt():
    client = genai.Client()
    response = client.models.generate_content(model="gemini-2.5-flash", contents="Explain how AI works in a few words")
    print(response.text)