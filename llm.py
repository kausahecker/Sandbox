from dotenv import load_dotenv
from google import genai

load_dotenv()
client=genai.Client(api_key="AIzaSyB_niCHDAMViEcUNORvwy37b27zQ1D4jAs")

def chat(query:str)->str:
    
    history=[{
        "role":"system",
        "parts":[{
            "text":"SYSTEM PROMPT"
        }]
    },{
        "role":"user",
        "parts":[{
            "text":query
        }]
    }]

    response=client.models.generate_content(model="gemini-2.5-flash-lite",contents=history)
    reply=response.text

    return reply