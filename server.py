import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def generate_recommendation(query: str):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    return response.text

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/model/recommend")
def recommend(query_request: QueryRequest):
    query = query_request.query  
    response = generate_recommendation(query) 
    print(response)
    return {"response": response}  
