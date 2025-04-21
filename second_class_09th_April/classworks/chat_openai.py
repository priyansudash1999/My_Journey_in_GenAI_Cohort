from dotenv import load_dotenv
from openai import OpenAI


client = OpenAI()
load_dotenv()

response = client.chat.completions.create(
  model= 'gpt-4',
  messages= [
    {"role" : "user", "content": " What is 2+2*0 ?"}
  ]
)

print(response.choices[0].message.content)

# It cannot work 