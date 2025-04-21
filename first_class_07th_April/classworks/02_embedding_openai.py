from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

text = 'I am Priyansu'
response = client.embeddings.create(
  input = text,
  model = 'text-embedding-3-small'
)

print("Vector embeddings", response.data[0].embedding)