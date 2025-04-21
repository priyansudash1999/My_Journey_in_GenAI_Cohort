from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

system_prompt = """
  You are an AI assistant who is expert in breaking down the complex problem and then resolve the problem step by step.
  For the given user input, analize the problem and breakdown the problem into step by step solution.
  Atleast think 5-6 steps on how to solve the problem before solving it down.

  The steps are you get a user input, you analyse, you think, you think again and again for several steps then return the answer.
  Follow the steps in sequence that is "analyze", "think", "ouput", "validate" , "Result", "output"

  Rules:-
  1) Follow the strict JSON output as per Output Schema
  2) Always perform one step at a time and wait for next input
  3) Carefully analyse the user query

  Output Format:- 
  {{step: "string", content: "string"}}

  Examples:-
  INPUT - What is 2+2 ?
  OUTPUT - {{step: "analyze", content: "The user is interested  in math query and he is asking a simple math arithmetic operation"}}
  OUTPUT- {{step: "think", content: "To perform the addition I must go from left tio right and all the operands"}}
  OUTPUT- {{step: "output", content: "4"}}
  OUTPUT- {{step: "validate", content: "seems like 4 is correct answer for 2+2"}}
  OUTPUT- {{step: "result", content: "2+2 = 4 and that is calculted by adding all numbers"}}
"""

result = client.chat.completions.create(
  model= "gpt-3.5-turbo",
  response_format= {"type": "json_object"},
  messages= [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What is 3*2*4/3 ? "},


    # 

    {"role": "assistant", "content": json.dumps({ "step": "analyze", "content": "The user is asking a math query and wants to evaluate a simple arithmetic expression."})},
    {"role": "assistant", "content": json.dumps({"step": "think", "content": "To solve the expression 3*2*4/3, I need to follow the order of operations which is multiplication and division from left to right."}  )},
    {"role": "assistant", "content": json.dumps({"step": "output", "content": "8"})},
    {"role": "assistant", "content": json.dumps({"step": "validate", "content": "The result of 3*2*4/3 is calculated as (3*2*4)/3 = 24/3 = 8."})},
    {"role": "assistant", "content": json.dumps({"step": "result", "content": "3*2*4/3 = 8 and that is calculated by performing multiplication and division operations."})},
  ]
)

print(result.choices[0].message.content)