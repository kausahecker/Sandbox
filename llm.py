from google import genai
import os

class LLM:
    def __init__(self,name:str,sys_prompt:str,type:str):
        self.client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.name=name
        self.sys_prompt=sys_prompt

    def chat(self,query:str,history:list[dict]=None)->str:
        if not history or len(history)==0:
            history=[{
                "role":"system",
                "parts":[{
                    "text":self.sys_prompt
                }]
            },{
                "role":"user",
                "parts":[{
                    "text":query
                }]
            }]
        response=self.client.models.generate_content(model="gemini-2.5-flash-lite",contents=history)
        reply=response.text
        history.append({
            "role":"assistant",
            "parts":[{
                "text":reply
            }]
        })
        return reply,history