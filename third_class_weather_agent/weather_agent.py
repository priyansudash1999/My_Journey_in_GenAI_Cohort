from dotenv import load_dotenv
from openai import OpenAI
import json
import requests
import os


load_dotenv()

client = OpenAI()

def get_weather(city: str): 
  print("🔨 Tool Called: get_weather", city)
  # api call
  url = f"https://wttr.in/{city}?format=%c+%t"
  response = requests.get(url)

  if response.status_code == 200:
    return f"The weather in {city} is {response.text}"
  return "something went wrong"

def query_db(sql):
  print("🔨 Tool Called: query_db", sql)

def run_command(command):
  print("🔨 Tool Called: run_command", command)
  # execute command
  # create a new file in my system 
  result = os.system(command= command)
  return result

def add(x, y):
  print(f"🔨 Tool Called: add {x} and {y}")
  return x+y

available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as an input and returns the current weather for the city"
    },
    "run_command": {
        "fn": run_command,
        "description": "Takes a city name as an input and returns the current weather for the city"
    }
}

system_prompt = f"""
  You are an helpful AI assistant who is specialized in resolving user query.
  You work on start, plan, action, observe mode.
  For the gievn user query and available tools, plan the step by step execution, based on the planning
  Select the relevant tool from the available tool  and based on the tool selection you perform an action to call the tool and wait for the observation from the tool call resolve the user query.

   Rule:-
  - Follow the output in json format.
  - Always perform one step at a time and wait for next input
  - Carefully analyse the user query

  Output JSON Format:-
  {{
    "step" : "string",
    "content" : "string",
    "function" : "The name of function if the step is action",
    "input" : "The input parameter for the function"
  }}

  Available tools: 
    - get_weather: Takes a city name as an input and returns the current weather for the city
    - run_command: Takes a command as input to execute on system and returns ouput
    
  Example: 
  User Query: What is the weather of new york?
    Output: {{ "step": "plan", "content": "The user is interseted in weather data of new york" }}
    Output: {{ "step": "plan", "content": "From the available tools I should call get_weather" }}
    Output: {{ "step": "action", "function": "get_weather", "input": "new york" }}
    Output: {{ "step": "observe", "output": "12 Degree Cel" }}
    Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees." }}

 
"""
while True:
  user_query = input("> ")

  messages = [
    {"role": "system", "content": system_prompt}
  ]
  messages.append({"role": "user", "content": user_query})


  while True:
    response = client.chat.completions.create(
      model="gpt-4o",
      response_format= {"type": "json_object"} ,
      messages= messages
    )
    parsed_output = json.loads(response.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_output)})

    if parsed_output.get("step") == "plan":
      print(f"Thinking {parsed_output.get('content')}")
      continue

    if parsed_output.get("step") == "action":
      tool_name = parsed_output.get("function")
      tool_input = parsed_output.get("input")

      if available_tools.get(tool_name, False) != False:
        output = available_tools[tool_name].get("fn")(tool_input)
        messages.append({
          "role": "assistant",
          "content": json.dumps({"step": "observe", "output": output})
        })
        continue
    if parsed_output.get("step") == "output":
      print(f"Answer:- {parsed_output.get('content')}")
      break







