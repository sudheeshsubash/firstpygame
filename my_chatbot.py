import openai
import pyttsx3
engine = pyttsx3.init()

    


# Replace YOUR_API_KEY with your actual API key
openai.api_key = "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"


def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = ask_gpt(user_input)
    print("ChatGPT: " + response)
    engine.say(response)
    engine.runAndWait()
