import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "AIzaSyAKs95vFXMbMYyhuQ4dgQazHNlv14rWcJY")
genai.configure(api_key=GOOGLE_API_KEY)

class BusinessPlanRequest(BaseModel):
    business_idea: str
    industry: str = "General"

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "KEDIN AI Backend is running"}

@app.post("/business-plan")
async def business_plan(request: BusinessPlanRequest):
    try:
        model = genai.GenerativeModel('gemma-4')
        prompt = f"""You are an expert business consultant. Write a detailed business plan for the following idea in Kano, Nigeria.
        Business Idea: {request.business_idea}
        Industry: {request.industry}
        Include sections: Executive Summary, Company Description, Market Analysis, Organization, Products/Services, Marketing Strategy, Financial Projections, Conclusion."""
        response = model.generate_content(prompt)
        return {"plan": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/market-survey")
async def market_survey(request: PromptRequest):
    model = genai.GenerativeModel('gemma-4')
    prompt = f"Create a comprehensive market survey questionnaire for a business idea: {request.prompt}. Include questions about demographics, needs, competition, and pricing. Also provide a brief analysis framework."
    response = model.generate_content(prompt)
    return {"survey": response.text}

@app.post("/courses")
async def courses(request: PromptRequest):
    model = genai.GenerativeModel('gemma-4')
    prompt = f"Recommend an 8-week entrepreneurship curriculum for someone interested in: {request.prompt}. List weekly topics, learning outcomes, and practical assignments."
    response = model.generate_content(prompt)
    return {"courses": response.text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
