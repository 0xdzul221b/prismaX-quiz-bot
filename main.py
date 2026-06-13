from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import random

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
        body {
            /* Smooth mesh glow using your exact color codes */
            background: radial-gradient(circle at 10% 20%, rgba(237, 228, 213, 0.15) 0%, transparent 45%),
                        radial-gradient(circle at 90% 80%, rgba(149, 121, 91, 0.2) 0%, transparent 50%),
                        radial-gradient(circle at center, #14110f 0%, #080605 100%);
            background-color: #080605;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 15px;
            box-sizing: border-box;
            overflow: hidden;
        }
        
        /* Premium Glowing Glassmorphism Quiz Card */
        .quiz-card {
            background: rgba(24, 20, 18, 0.7);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border-radius: 16px;
            padding: 28px;
            max-width: 430px;
            width: 100%;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8),
                        0 0 30px rgba(149, 121, 91, 0.05);
            position: relative;
            border: 1px solid rgba(237, 228, 213, 0.08);
        }
        
        /* Top border gradient accent matching your profile color themes */
        .quiz-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 4px;
            background: linear-gradient(90deg, rgb(149, 121, 91), rgb(237, 228, 213));
            border-radius: 16px 16px 0 0;
        }
        
        .header {
            text-align: center;
            margin-bottom: 22px;
        }
        .header h2 {
            letter-spacing: 3px;
            font-size: 21px;
            margin: 0;
            color: rgb(237, 228, 213);
            text-transform: uppercase;
            font-weight: 800;
            text-shadow: 0 2px 8px rgba(237, 228, 213, 0.2);
        }
        .subtitle {
            font-size: 11px;
            color: rgba(237, 228, 213, 0.6);
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            font-weight: 600;
        }
        
        .timer-bar-container {
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            height: 5px;
            border-radius: 3px;
            margin-bottom: 24px;
            overflow: hidden;
        }
        .timer-bar {
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, rgb(149, 121, 91), rgb(237, 228, 213));
            transition: width 1s linear;
        }
        
        .question {
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 24px;
            color: #f5f4f2;
            font-weight: 500;
        }
        .options-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        /* Modern Button Styling utilizing your core colors */
        .option-btn {
            background: rgba(36, 30, 27, 0.6);
            border: 1px solid rgba(237, 228, 213, 0.1);
            color: #e5e3df;
            padding: 15px;
            border-radius: 10px;
            text-align: left;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .option-btn:hover {
            background: rgba(149, 121, 91, 0.2);
            border-color: rgb(149, 121, 91);
            color: #ffffff;
            transform: translateY(-1px);
        }
        
        /* Feedback State Overrides */
        .correct {
            background: rgba(46, 204, 113, 0.2) !important;
            border-color: #2ecc71 !important;
            color: #2ecc71 !important;
            font-weight: bold;
            box-shadow: 0 0 12px rgba(46, 204, 113, 0.15);
        }
        .wrong {
            background: rgba(231, 76, 60, 0.2) !important;
            border-color: #e74c3c !important;
            color: #e74c3c !important;
        }
        
        .score-screen {
            text-align: center;
            padding: 10px 0;
        }
        .btn-group {
            display: flex;
            flex-direction: column;
            gap: 12px;
            justify-content: center;
            align-items: center;
            margin-top: 24px;
        }
        
        .restart-btn {
            background: linear-gradient(90deg, rgb(149, 121, 91), rgb(237, 228, 213));
            color: #080605;
            border: none;
            padding: 14px 28px;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 700;
            width: 100%;
            max-width: 220px;
            transition: opacity 0.2s ease;
        }
        .restart-btn:hover {
            opacity: 0.95;
        }
        
        .x-share-btn {
            background: #000000;
            color: #ffffff;
            border: 1px solid rgba(237, 228, 213, 0.2);
            padding: 14px 28px;
            border-radius: 10px;
            cursor: pointer;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 100%;
            max-width: 220px;
            text-decoration: none;
            box-sizing: border-box;
            transition: all 0.2s ease;
        }
        .x-share-btn:hover {
            border-color: rgb(237, 228, 213);
            background: rgba(255,255,255,0.03);
        }
    </style>
</head>
<body>
    <div class="quiz-card" id="quiz-box">
        <div class="header">
            <h2>PRISMAX</h2>
            <div class="subtitle">🔒 PHYSICAL AI & DATA SHIELDED QUIZ</div>
        </div>
        <div id="quiz-body">
            <div class="timer-bar-container"><div class="timer-bar" id="t-bar"></div></div>
            <div class="question" id="q-text">Loading Quiz Data...</div>
            <div class="options-container" id="options-box"></div>
        </div>
    </div>
    <script>
        let quizzes=[],currentIdx=0,score=0,timeLeft=15,timerInterval=null,canClick=true,isTabActive=true;
        const audioCtx=new(window.AudioContext||window.webkitAudioContext)();

        function playRobotSound(type) {
            try {
                let osc=audioCtx.createOscillator();
                let gain=audioCtx.createGain();
                osc.connect(gain); gain.connect(audioCtx.destination);
                if(type==='correct') {
                    osc.type='triangle';
                    osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); 
                    osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1); 
                    gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.2);
                } else if(type==='wrong') {
                    osc.type='sawtooth';
                    osc.frequency.setValueAtTime(130, audioCtx.currentTime); 
                    osc.frequency.linearRampToValueAtTime(60, audioCtx.currentTime + 0.3); 
                    gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.3);
                }
            } catch(e){}
        }

        async function fetchQuizzes(){
            try{
                let e=await fetch("/get-quiz"),t=await e.json();
                quizzes=t.quizzes,currentIdx=0,score=0,showQuestion()
            }catch(e){
                document.getElementById("q-text").innerText="Failed to initialize quiz module."
            }
        }
        
        function startTimer(){
            clearInterval(timerInterval);
            timeLeft=15; canClick=true; updateTimerBar();
            timerInterval=setInterval(()=>{
                if(!isTabActive) return;
                timeLeft--; updateTimerBar();
                if(timeLeft<=0){ clearInterval(timerInterval); canClick=false; autoTimeOut() }
            },1000)
        }
        
        function updateTimerBar(){
            document.getElementById("t-bar").style.width=(timeLeft/15)*100+"%"
        }
        
        function showQuestion(){
            if(currentIdx>=quizzes.length){ showResult(); return }
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
            clearInterval(timerInterval); canClick=false;
            let o=document.querySelectorAll(".option-btn");
            o.forEach(e=>e.disabled=!0);
            if(t===n){ e.classList.add("correct"); playRobotSound('correct'); score++ }
            else { e.classList.add("wrong"); playRobotSound('wrong'); o.forEach(e=>{if(e.innerText===n)e.classList.add("correct")}) }
            setTimeout(()=>{currentIdx++,showQuestion()},1400)
        }
        
        function autoTimeOut(){
            playRobotSound('wrong');
            let e=quizzes[currentIdx].answer;
            document.querySelectorAll(".option-btn").forEach(t=>{
                t.disabled=!0;
                if(t.innerText===e)t.classList.add("correct"); else t.classList.add("wrong");
            });
            setTimeout(()=>{currentIdx++,showQuestion()},1400)
        }
        
        function showResult(){
            clearInterval(timerInterval);
            let shareText=encodeURIComponent(`I just scored ${score}/10 on the PRISMAX Physical AI Quiz! 🧠🚀\\n\\nTry it here: ${window.location.origin}`);
            let xUrl= `https://x.com/intent/tweet?text=${shareText}`;
            document.getElementById("quiz-body").innerHTML=`
                <div class="score-screen">
                    <h3 style='color:rgb(237, 228, 213);margin-bottom:10px;'>Quiz Completed!</h3>
                    <p style="font-size: 26px; color:rgb(237, 228, 213); margin-bottom:25px; font-weight:800;">Your Score: ${score} / ${quizzes.length}</p>
                    <div class="btn-group">
                        <a class="x-share-btn" href="${xUrl}" target="_blank">Share on X</a>
                        <button class="restart-btn" onclick="location.reload()">Play Again</button>
                    </div>
                </div>`
        }

        document.addEventListener("visibilitychange", () => {
            if (document.hidden) {
                isTabActive = false;
            } else {
                isTabActive = true;
            }
        });

        fetchQuizzes();
    </script>
</body>
</html>"""
    return html_content
