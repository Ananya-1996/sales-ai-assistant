from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Query
from adk_agent.weather_app.agent import run_agent

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Sales AI Assistant</title>

        <style>
            body {
                margin: 0;
                font-family: Arial;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .chat-container {
                width: 450px;
                height: 600px;
                background: #1e293b;
                border-radius: 12px;
                display: flex;
                flex-direction: column;
                padding: 15px;
                box-shadow: 0 0 20px rgba(0,0,0,0.6);
            }

            .header {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }

            .messages {
                flex: 1;
                overflow-y: auto;
                padding: 10px;
                scroll-behavior: smooth;
            }

            .msg {
                padding: 10px;
                margin: 8px 0;
                border-radius: 10px;
                max-width: 75%;
                line-height: 1.4;
            }

            .user {
                background: #3b82f6;
                margin-left: auto;
            }

            .bot {
                background: #334155;
            }

            .input-area {
                display: flex;
                gap: 10px;
                margin-top: 10px;
                align-items: center;
            }

            textarea {
                flex: 1;
                padding: 10px;
                border-radius: 8px;
                border: none;
                resize: none;
                height: 40px;
                max-height: 120px;
                overflow-y: auto;
                font-family: Arial;
                outline: none;
            }

            button {
                padding: 10px 16px;
                border: none;
                background: #22c55e;
                color: white;
                border-radius: 8px;
                cursor: pointer;
            }

            a {
                color: #38bdf8;
                font-weight: bold;
                text-decoration: none;
            }
        </style>
    </head>

    <body>
        <div class="chat-container">
            <div class="header">🤖 Sales AI Assistant</div>

            <div id="messages" class="messages"></div>

            <div class="input-area">
                <textarea id="query" placeholder="Ask sales insights..." rows="1"></textarea>
                <button onclick="sendMessage()">Send</button>
            </div>
        </div>

        <script>
            const textarea = document.getElementById("query");

            // ✅ Auto-resize
            textarea.addEventListener("input", () => {
                textarea.style.height = "auto";
                textarea.style.height = textarea.scrollHeight + "px";
            });

            // ✅ Enter to send
            textarea.addEventListener("keydown", function(e) {
                if (e.key === "Enter" && !e.shiftKey) {
                    e.preventDefault();
                    sendMessage();
                }
            });

            async function sendMessage() {
                let input = document.getElementById("query");
                let message = input.value.trim();

                if (!message) return;

                let messages = document.getElementById("messages");

                // user message
                messages.innerHTML += `<div class="msg user">${message}</div>`;

                // typing animation
                let typing = document.createElement("div");
                typing.className = "msg bot";
                typing.innerText = "Typing...";
                messages.appendChild(typing);

                input.value = "";
                input.style.height = "40px";

                try {
                    let res = await fetch(`/ask?query=${encodeURIComponent(message)}`);
                    let data = await res.json();

                    typing.remove();

                    messages.innerHTML += `
                    <div class="msg bot">
                        📍 <b>${data.city}</b><br><br>

                        🌤 ${data.temp}°C | Wind ${data.wind}<br><br>

                        🧠 ${data.decision}<br>
                        📌 ${data.reason}<br><br>

                        ⏰ ${data.time}<br>
                        📊 ${data.priority}<br><br>

                        <a href="${data.link}" target="_blank">📅 Open Calendar</a>
                    </div>
                    `;

                    messages.scrollTop = messages.scrollHeight;

                } catch (e) {
                    typing.remove();
                    messages.innerHTML += `<div class="msg bot">❌ Error fetching response</div>`;
                }
            }
        </script>
    </body>
    </html>
    """


@app.get("/ask")
def ask(query: str = Query(...)):
    return run_agent(query)
