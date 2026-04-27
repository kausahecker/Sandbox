from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key="AIzaSyB_niCHDAMViEcUNORvwy37b27zQ1D4jAs")
def chat():
    print("Sandbox LLM — type 'exit' to quit\n")
    history = []
 
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
 
        history.append({"role": "user", "parts": [{"text": user_input}]})
 
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=history,
        )
      
        reply = response.text
        print(f"\nGemini: {reply}\n")
 
        history.append({"role": "model", "parts": [{"text": reply}]})
 
if __name__ == "__main__":
    chat()

    
#from google import genai

#client=genai.Client(api_key="AIzaSyB_niCHDAMViEcUNORvwy37b27zQ1D4jAs")

#def query_gemini(prompt:str)->str:
    #response=client.models.generate_content(model="gemini-2.5-flash-lite",contents=prompt)
    #return response.text