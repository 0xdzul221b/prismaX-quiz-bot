from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random
import requests
import os

app = FastAPI()

# CORS Middleware for Frontend Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
QUIZ_BANK = [
    {"id": 1, "question": "What is PrismaX?", "options": ["A crypto exchange", "A service layer for Physical AI", "A gaming platform", "A cloud provider"], "answer": "A service layer for Physical AI"},
    {"id": 2, "question": "What are the three core pillars of PrismaX?", "options": ["Compute, Storage, Network", "Data, Teleoperation, Models", "AI, Blockchain, Gaming", "Robots, NFTs, DeFi"], "answer": "Data, Teleoperation, Models"},
    {"id": 3, "question": "What is teleoperation?", "options": ["Autonomous robot learning", "Robot manufacturing", "Remote control of robots by humans", "Robot maintenance"], "answer": "Remote control of robots by humans"},
    {"id": 4, "question": "Why does PrismaX use human-in-the-loop operations?", "options": ["To reduce electricity costs", "To generate high-quality training data", "To replace robots", "To create NFTs"], "answer": "To generate high-quality training data"},
    {"id": 5, "question": "What major challenge is PrismaX solving?", "options": ["Slow internet speeds", "Lack of robotics hardware", "Shortage of high-quality robotics data", "Cloud storage issues"], "answer": "Shortage of high-quality robotics data"},
    {"id": 6, "question": "What improves robotics models in the PrismaX flywheel?", "options": ["More advertisements", "More data collection", "More token supply", "More servers"], "answer": "More data collection"},
    {"id": 7, "question": "PrismaX mainly focuses on which type of AI?", "options": ["Generative AI", "Physical AI", "Social AI", "Financial AI"], "answer": "Physical AI"},
    {"id": 8, "question": "Which venture firm led PrismaX's funding round?", "options": ["Sequoia Capital", "Y Combinator", "a16z CSX", "Tiger Global"], "answer": "a16z CSX"},
    {"id": 9, "question": "How much funding did PrismaX raise?", "options": ["$5M", "$8M", "$11M", "$20M"], "answer": "$11M"},
    {"id": 10, "question": "What is essential for training better robotics models?", "options": ["More tokens", "High-quality real-world data", "More advertisements", "Faster Wi-Fi"], "answer": "High-quality real-world data"},
    {"id": 11, "question": "Which program did PrismaX join in 2026?", "options": ["Google Startups", "NVIDIA Inception Program", "AWS Activate", "Microsoft Founders Hub"], "answer": "NVIDIA Inception Program"},
    {"id": 12, "question": "Which factor affects robotics data usefulness?", "options": ["Robot embodiment", "Company logo", "Token price", "Domain name"], "answer": "Robot embodiment"},
    {"id": 13, "question": "What future workforce model is PrismaX building?", "options": ["Crypto mining network", "Labor marketplace for robot operators", "Ride-sharing platform", "Freelance coding network"], "answer": "Labor marketplace for robot operators"},
    {"id": 14, "question": "What is a key benefit of teleoperation?", "options": ["Increases social media followers", "Scalable data collection", "Reduces internet usage", "Creates cryptocurrencies"], "answer": "Scalable data collection"},
    {"id": 15, "question": "Which robots can use PrismaX's platform?", "options": ["Only humanoids", "Only robotic arms", "Only quadrupeds", "Multiple robot types including humanoids, arms, and quadrupeds"], "answer": "Multiple robot types including humanoids, arms, and quadrupeds"},
    {"id": 16, "question": "How does PrismaX describe itself?", "options": ["The service layer for Physical AI", "The blockchain of gaming", "The future of social media", "The largest cloud provider"], "answer": "The service layer for Physical AI"},
    {"id": 17, "question": "Why is robotics considered data-deficient?", "options": ["Too many datasets exist", "Robotics datasets are much smaller than AI datasets", "Robots don't need data", "Data is free everywhere"], "answer": "Robotics datasets are much smaller than AI datasets"},
    {"id": 18, "question": "What is PrismaX's long-term vision?", "options": ["Launching a meme coin", "Supporting millions of autonomous robots", "Building smartphones", "Creating a search engine"], "answer": "Supporting millions of autonomous robots"},
    {"id": 19, "question": "How does PrismaX plan to reward data contributors?", "options": ["Through fair-use value sharing", "Free hardware only", "Social media badges only", "Free internet access"], "answer": "Through fair-use value sharing"},
    {"id": 20, "question": "What best describes PrismaX's mission?", "options": ["Bringing human skills to robots", "Bringing robots to Mars", "Replacing all workers", "Building video games"], "answer": "Bringing human skills to robots"}
]
@app.get("/")
def home():
    return {"message": "PrismaX Quiz Bot Backend is Online!"}
@app.get("/get-quiz")
def get_quiz():
    random_quiz = random.sample(QUIZ_BANK, 10)
    return {"status": "success", "total": len(random_quiz), "quizzes": random_quiz}
@app.post("/ask-ai")
def ask_ai(user_message: str):
    if not OPENROUTER_API_KEY:
        raise HTTPException(status_code=500, detail="OpenRouter API Key set kora nai!")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/llama-3-8b-instruct:free",
        "messages": [
            {"role": "system", "content": "Tumi ekta PrismaX Quiz Bot Assistant."},
            {"role": "user", "content": user_message}
        ]
    }
    
    response = requests.post(OPENROUTER_URL, headers=headers, json=data)
    return response.json()
