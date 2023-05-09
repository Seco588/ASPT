import openai

def init_ai(api_key):
    openai.api_key = api_key

def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
