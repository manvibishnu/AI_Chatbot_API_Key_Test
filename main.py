import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(prompt):
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
        #messages=[{"role": "user", "content": prompt}]
    )

    return response.output_text.strip()
    #return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Me: ")
        if user_input.lower() in ["quit", "exit", "stop", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)