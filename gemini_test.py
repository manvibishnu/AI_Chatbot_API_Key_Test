import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def chat_with_gemini(prompt):
    response = client.chat.completions.create(
        model="gemini-3.8-flash",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("Me: ")

        if user_input.lower() in ["quit", "exit", "stop", "bye"]:
            break

        response = chat_with_gemini(user_input)
        print("Gemini:", response)