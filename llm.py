from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat(query:str,history:list[dict]=None)->str:
    if not history:
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
    history.append({
        "role":"assistant",
        "parts":[{
            "text":reply
        }]
    })
    return reply,history