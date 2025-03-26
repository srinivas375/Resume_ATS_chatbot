from langchain_groq import ChatGroq
from langchain_core.exceptions import LangChainException
from dotenv import load_dotenv

load_dotenv()

try:
    model = ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature = 0
    )
    
    print("LLM model initialized successfully")

except LangChainException as e:
    print("Langchain error :", e)
    
except Exception as e:
    print("An unknown error occured :", e)