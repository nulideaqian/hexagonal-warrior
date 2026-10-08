import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")

client = OpenAI(base_url=OPENAI_API_BASE, api_key=OPENAI_API_KEY)

if __name__ == "__main__":
    messages = []
    for i in range(5):
        user_input = input(">>> ")
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model=OPENAI_API_MODEL,
            messages=messages,
        )
        print(response.choices[0].message.content)
        messages.append(
            {"role": "assistant", "content": response.choices[0].message.content})
