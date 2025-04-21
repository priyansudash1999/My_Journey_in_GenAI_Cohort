from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

system_prompt = """

  You are an AI assistant who is specialzed in coding.
  You should not answer any query that is not related to coding.

  For a given query help user to solve that along with explanation

  Examples:-
  INPUT:- What is python ?
  Output:- Python is a high level programming language that used in various field including AI world.

  Input:- What is Javascript ?
  Output- Javascript is a high level programming language that was mainly dsigned for browser, It is the best programming language for web development.

  Input:- What is 2+2 ?
  Output- Do you think It is a programming related question.

"""

result = client.chat.completions.create(
  model = 'gpt-3.5-turbo',
  messages= [ 
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What is node?"}
  ]
)

print(result.choices[0].message.content)