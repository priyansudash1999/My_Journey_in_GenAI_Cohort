from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
# print(api_key) 

client = genai.Client(api_key=api_key)
res = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='What is 2+2*0 ?'
)
print(res.text)