from dotenv import load_dotenv

import llm
import tool_suite

def init():
    load_dotenv()
    tool_suite.init()

def chat():
    while True:
        pass