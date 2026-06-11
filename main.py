from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import random
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/get-quiz")
def get_quiz():
    return {"status": "success", "total": 10, "quizzes": random.sample(QUIZ_BANK, 10)}

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>PRISMAX | QUIZ</title>
    <style>
        body{background-color:#0b0c10;background-image:linear-gradient(rgba(18,18,24,.7) 1px,transparent 1px),linear-gradient(90deg,rgba(18,18,24,.7) 1px,transparent 1px);background-size:25px 25px;color:#fff;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;padding:15px;box-sizing:border-box}
        .quiz-card{background:rgba(23,23,28,.85);backdrop-filter:blur(10px);border-radius:12px;padding:25px;max-width:420px;width:100%;box-shadow:0 10px 30px rgba(0,0,0,.5);position:relative;border:1px solid rgba(255,255,255,.05)}
        .quiz-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#4285f4,#a733ff,#00f2fe);border-top-left-radius:12px;border-top-right-radius:12px}
        .header{text-align:center;margin-bottom:20px}
        .header h2{letter-spacing:2px;font-size:18px;margin:0;color:#e0e0e3;text-transform:uppercase}
        .subtitle{font-size:11px;color:#888893;margin-top:5px;text-transform:uppercase;letter-spacing:1px}
        .timer-bar-container{width:100%;background:rgba(255,255,255,0.05);height:4px;border-radius:2px;margin-bottom:20px;overflow:hidden}
        .timer-bar{width:100%;height:100%;background:linear-gradient(90deg,#00f2fe,#4285f4);transition:width 1s linear}
        .question{font-size:15px;line-height:1.5;margin-bottom:20px;color:#f1f1f5;font-weight:500}
        .options-container{display:flex;flex-direction:column;gap:12px}
        .option-btn{background:rgba(33,33,42,.9);border:1px solid rgba(255,255,255,.08);color:#d1d1d6;padding:14px;border-radius:8px;text-align:left;font-size:14px;cursor:pointer;transition:all .2s ease}
        .option-btn:hover{background:rgba(45,45,58,.9);border-color:rgba(255,255,255,.2)}
        .correct{background:rgba(46,204,113,.2)!important;border-color:#2ecc71!important;color:#2ecc71!important}
        .wrong{background:rgba(231,76,60,.2)!important;border-color:#e74c3c!important;color:#e74c3c!important}
        .score-screen{text-align:center}
        .btn-group{display:flex;flex-direction:column;gap:10px;justify-content:center;align-items:center;margin-top:20px}
        .restart-btn{background:linear-gradient(90deg,#4285f4,#a733ff);color:#fff;border:none;padding:12px 25px;border-radius:8px;cursor:pointer;font-weight:700;width:100%;max-width:200px}
        .x-share-btn{background:#000;color:#fff;border:1px solid rgba(255,255,255,0.2);padding:12px 25px;border-radius:8px;cursor:pointer;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;width:100%;max-width:200px;text-decoration:none}
        .x-share-btn:hover{background:#15181c;border-color:rgba(255,255,255,0.4)}
    </style>
</head>
<body>
    <div class="quiz-card" id="quiz-box">
        <div class="header">
            <h2>PRISMAX</h2>
            <div class="subtitle">🔒 PHYSICAL AI & DATA SHIELD QUIZ</div>
        </div>
        <div id="quiz-body">
            <div class="timer-bar-container"><div class="timer-bar" id="t-bar"></div></div>
            <div class="question" id="q-text">Loading Quiz...</div>
            <div class="options-container" id="options-box"></div>
        </div>
    </div>
    <script>
        let quizzes=[],currentIdx=0,score=0,timeLeft=15,timerInterval=null,canClick=true;
        async function fetchQuizzes(){
            try{
                let e=await fetch("/get-quiz"),t=await e.json();
                quizzes=t.quizzes,currentIdx=0,score=0,showQuestion()
            }catch(e){
                document.getElementById("q-text").innerText="Failed to load quiz. Try again."
            }
        }
        function startTimer(){
            clearInterval(timerInterval);
            timeLeft=15;
            canClick=true;
            updateTimerBar();
            timerInterval=setInterval(()=>{
                timeLeft--;
                updateTimerBar();
                if(timeLeft<=0){
                    clearInterval(timerInterval);
                    canClick=false;
                    autoTimeOut()
                }
            },1000)
        }
        function updateTimerBar(){
            let percentage=(timeLeft/15)*100;
            document.getElementById("t-bar").style.width=percentage+"%"
        }
        function showQuestion(){
            if(currentIdx>=quizzes.length){
                showResult();
                return
            }
            startTimer();
            let e=quizzes[currentIdx];
            document.getElementById("q-text").innerText=`Q${currentIdx+1}. ${e.question}`;
            let t=document.getElementById("options-box");
            t.innerHTML="",e.options.forEach(n=>{
                let o=document.createElement("button");
                o.className="option-btn",o.innerText=n,o.onclick=()=>checkAnswer(o,n,e.answer),t.appendChild(o)
            })
        }
        function checkAnswer(e,t,n){
            if(!canClick)return;
            clearInterval(timerInterval);
            canClick=false;
            let o=document.querySelectorAll(".option-btn");
            o.forEach(e=>e.disabled=!0);
            if(t===n){
                e.classList.add("correct");
                score++
            }else{
                e.classList.add("wrong");
                o.forEach(e=>{if(e.innerText===n)e.classList.add("correct")})
            }
            setTimeout(()=>{currentIdx++,showQuestion()},1500)
        }
        function autoTimeOut(){
            let e=quizzes[currentIdx].answer;
            let t=document.querySelectorAll(".option-btn");
            t.forEach(t=>{
                t.disabled=!0;
                if(t.innerText===e)t.classList.add("correct");
                else t.classList.add("wrong")
            });
            setTimeout(()=>{currentIdx++,showQuestion()},1500)
        }
        function showResult(){
            clearInterval(timerInterval);
            let shareText=encodeURIComponent(`I just scored ${score}/10 on the PRISMAX Physical AI Quiz! 🧠🚀\n\nTry it here: ${window.location.origin}`);
            let xUrl=`https://x.com/intent/tweet?text=${shareText}`;
            document.getElementById("quiz-body").innerHTML=`
                <div class="score-screen">
                    <h3>Quiz Completed!</h3>
                    <p style="font-size: 24px; color:#00f2fe; margin-bottom:25px;">Your Score: ${score} / ${quizzes.length}</p>
                    <div class="btn-group">
                        <a class="x-share-btn" href="${xUrl}" target="_blank">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                            Share on X
                        </a>
                        <button class="restart-btn" onclick="location.reload()">Play Again</button>
                    </div>
                </div>`
        }
        fetchQuizzes();
    </script>
</body>
</html>"""
    return html_content
