import openai
openai.api_key = "YOUR_API_KEY"

def ask_chatgpt(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Q: {question}\nA:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer
