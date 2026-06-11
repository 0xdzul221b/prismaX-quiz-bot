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
    <title>PRISMAX | OFFICIAL QUIZ</title>
    <style>
        body {
            background-color: #0d0d0d;
            background-image: linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
            background-size: 30px 30px;
            color: #FFFFFF;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 15px;
            box-sizing: border-box;
        }
        .quiz-card {
            background: #202020;
            border: 1px solid #3a3a3a;
            border-radius: 0px;
            padding: 35px 30px;
            max-width: 440px;
            width: 100%;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7);
            position: relative;
        }
        .header {
            text-align: left;
            margin-bottom: 25px;
            border-bottom: 1px solid #3a3a3a;
            padding-bottom: 15px;
        }
        .header h2 {
            font-size: 24px;
            font-weight: 700;
            letter-spacing: -0.5px;
            margin: 0;
            color: #DFD8D0;
        }
        .subtitle {
            font-size: 11px;
            color: #888888;
            margin-top: 6px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 600;
        }
        .timer-bar-container {
            width: 100%;
            background: #2d2d2d;
            height: 2px;
            margin-bottom: 25px;
        }
        .timer-bar {
            width: 100%;
            height: 100%;
            background: #DFD8D0;
            transition: width 1s linear;
        }
        .question {
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 25px;
            color: #FFFFFF;
            font-weight: 500;
            letter-spacing: -0.1px;
        }
        .options-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .option-btn {
            background: #181818;
            border: 1px solid #333333;
            color: #DFD8D0;
            padding: 15px 18px;
            border-radius: 0px;
            text-align: left;
            font-size: 14px;
            cursor: pointer;
            font-weight: 400;
            transition: background 0.15s ease, border-color 0.15s ease;
        }
        .option-btn:hover {
            background: #262626;
            border-color: #555555;
        }
        .correct {
            background: #1b3a24 !important;
            border-color: #2ecc71 !important;
            color: #2ecc71 !important;
            font-weight: 600;
        }
        .wrong {
            background: #3d1c1c !important;
            border-color: #e74c3c !important;
            color: #e74c3c !important;
            font-weight: 600;
        }
        .score-screen {
            text-align: center;
            padding: 10px 0;
        }
        .score-title {
            font-size: 20px;
            font-weight: 600;
            color: #DFD8D0;
            margin-bottom: 10px;
        }
        .score-num {
            font-size: 42px;
            font-weight: 700;
            color: #FFFFFF;
            margin: 15px 0 30px 0;
            letter-spacing: -1px;
        }
        .btn-group {
            display: flex;
            flex-direction: column;
            gap: 12px;
            align-items: center;
        }
        .restart-btn {
            background: #DFD8D0;
            color: #202020;
            border: none;
            padding: 14px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: opacity 0.15s ease;
        }
        .restart-btn:hover {
            opacity: 0.9;
        }
        .x-share-btn {
            background: transparent;
            color: #DFD8D0;
            border: 1px solid #444444;
            padding: 14px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            text-decoration: none;
            box-sizing: border-box;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: background 0.15s ease;
        }
        .x-share-btn:hover {
            background: #282828;
            border-color: #666666;
        }
    </style>
</head>
<body>
    <div class="quiz-card" id="quiz-box">
        <div class="header">
            <h2>PRISMAX</h2>
            <div class="subtitle">PHYSICAL AI INTERACTION PROTOCOL</div>
        </div>
        <div id="quiz-body">
            <div class="timer-bar-container"><div class="timer-bar" id="t-bar"></div></div>
            <div class="question" id="q-text">Initializing parameters...</div>
            <div class="options-container" id="options-box"></div>
        </div>
    </div>
    <script>
        let quizzes=[],currentIdx=0,score=0,timeLeft=15,timerInterval=null,canClick=true;
        const audioCtx=new(window.AudioContext||window.webkitAudioContext)();

        function playRobotSound(type) {
            try {
                let osc=audioCtx.createOscillator();
                let gain=audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                if(type==='correct') {
                    osc.type='triangle';
                    osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); // D5
                    osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1); // A5 (Chime synth)
                    gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.25);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.25);
                } else if(type==='wrong') {
                    osc.type='sawtooth';
                    osc.frequency.setValueAtTime(150, audioCtx.currentTime); 
                    osc.frequency.linearRampToValueAtTime(70, audioCtx.currentTime + 0.3); // Downward metallic buzz
                    gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.35);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.35);
                }
            } catch(e){}
        }

        async function fetchQuizzes(){
            try{
                let e=await fetch("/get-quiz"),t=await e.json();
                quizzes=t.quizzes,currentIdx=0,score=0,showQuestion()
            }catch(e){
                document.getElementById("q-text").innerText="Connection lost. Protocol execution failed."
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
            document.getElementById("q-text").innerText=`DATA_SHEETS_0${currentIdx+1} // ${e.question}`;
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
                e.classList.add('correct');
                playRobotSound('correct');
                score++
            }else{
                e.classList.add('wrong');
                playRobotSound('wrong');
                o.forEach(e=>{if(e.innerText===n)e.classList.add('correct')})
            }
            setTimeout(()=>{currentIdx++,showQuestion()},1600)
        }
        function autoTimeOut(){
            playRobotSound('wrong');
            let e=quizzes[currentIdx].answer;
            let t=document.querySelectorAll(".option-btn");
            t.forEach(t=>{
                t.disabled=!0;
                if(t.innerText===e)t.classList.add('correct');
                else t.classList.add('wrong')
            });
            setTimeout(()=>{currentIdx++,showQuestion()},1600)
        }
        function showResult(){
            clearInterval(timerInterval);
            let shareText=encodeURIComponent(`PrismaX Physical AI Evaluation Metrics Complete.\n\nScore Matrix: [ ${score} / 10 ]\n\nExecute protocol here: ${window.location.origin}`);
            let xUrl=`https://x.com/intent/tweet?text=${shareText}`;
            document.getElementById("quiz-body").innerHTML=`
                <div class="score-screen">
                    <div class="score-title">EVALUATION METRICS</div>
                    <div class="score-num">${score} / ${quizzes.length}</div>
                    <div class="btn-group">
                        <button class="restart-btn" onclick="location.reload()">Re-Run Analytics</button>
                        <a class="x-share-btn" href="${xUrl}" target="_blank">
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="#DFD8D0"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                            Share Logs on X
                        </a>
                    </div>
                </div>`
        }
        fetchQuizzes();
    </script>
</body>
</html>"""
    return html_content
