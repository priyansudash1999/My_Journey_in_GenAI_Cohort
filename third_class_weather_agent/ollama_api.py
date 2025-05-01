from fastapi import FastAPI
from ollama import Client
from fastapi import Body

app = FastAPI()

client = Client(host='http://localhost:11434')

client.pull('gemma3:1b')

@app.post("/chat")
def chat(message: str = Body(..., description= "Chat Message")):
    try:
        response = client.chat(model="gemma3:1b", messages=[
            {"role": "user", "content": "Hey there"}
        ])
    
        print("Response from Ollama: ", response)

        if 'message' in response:
            message = response['message']
            print(message) 
            
            return {"response": message.content}
        else:
            return {"error": "No 'message' found in response"}
    
    except Exception as e:
        # Catch and log any errors
        return {"error": str(e)}
