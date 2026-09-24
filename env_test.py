import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("MY_NAME")

print(name)

api_key = os.getenv("OPEN_API_KEY")

if api_key:
    print("API key was loaded.")
else:
    print("API key not found.")