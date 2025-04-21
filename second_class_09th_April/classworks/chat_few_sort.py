# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")
# # print(api_key) 

# client = genai.Client(api_key=api_key)
# res = client.models.generate_content(
#     model='gemini-2.0-flash-001',
#     contents='What is 2+2*0 ?'
# )
# print(res.text)



from openai import OpenAI
import os

client = OpenAI(
  api_key= os.getenv("GEMINI_API_KEY"),
  base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)
response = client.chat.completions.create(
  model= 'gemini-2.0-flash',
  messages= [
    {"role": "system", "content": "You are an ai assistant who is a English to Hindi translator"},
    {"role" : "user", "content": " What is 2+2*0 ?"}
  ]
)

print(response.choices[0].message.content)