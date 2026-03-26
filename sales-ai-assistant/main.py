
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Query
from adk_agent.weather_app.agent import run_agent

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head><title>Sales AI Assistant</title></head>
    <body style="font-family: Arial; text-align:center;">
        <h1>🤖 Sales AI Assistant</h1>
        <input id="query" placeholder="Ask sales insights..." />
        <button onclick="sendMessage()">Send</button>
        <div id="messages"></div>
        <script>
            async function sendMessage() {
                let q = document.getElementById("query").value;
                let res = await fetch(`/ask?query=${encodeURIComponent(q)}`);
                let data = await res.json();
                document.getElementById("messages").innerHTML += 
                    `<p><b>You:</b> ${q}</p><p><b>AI:</b> ${data.response}</p>`;
            }
        </script>
    </body>
    </html>
    """

@app.get("/ask")
def ask(query: str = Query(...)):
    return {"response": run_agent(query)}
