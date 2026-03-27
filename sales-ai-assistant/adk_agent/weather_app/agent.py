
from datetime import datetime, timedelta
from calendar_utils import create_event
import re
import requests
import os


# 🔑 API KEY from environment
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


# 🧠 Smart city detection
def extract_city(query: str):
    query = query.lower()

    match = re.search(r"in ([a-zA-Z ]+)", query)
    if match:
        return match.group(1).strip().title()

    ignore = ["schedule", "meeting", "call", "with", "for", "a", "the"]
    words = [w for w in query.split() if w not in ignore]

    if words:
        return words[-1].title()

    return "Bangalore"


# 🌤️ Real weather API
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]

        return temp, wind

    except Exception as e:
        print("Weather API Error:", e)
        return 26, 5  # fallback


# 🧠 Meeting decision
def meeting_decision(temp, wind):
    if temp > 35 or wind > 20:
        return "💻 ONLINE", "Extreme weather conditions"
    elif temp < 15:
        return "💻 ONLINE", "Too cold"
    else:
        return "🏢 OFFLINE", "Pleasant weather"


# 📊 Priority detection
def get_priority(query):
    query = query.lower()
    if "vip" in query:
        return "🔥 High Priority"
    elif "client" in query:
        return "⚡ Medium Priority"
    return "🟢 Normal"


# ⏰ Smart scheduling
def get_meeting_time():
    now = datetime.now()

    if now.hour >= 18:
        start = now.replace(hour=9, minute=0, second=0) + timedelta(days=1)
    elif now.hour < 9:
        start = now.replace(hour=9, minute=0, second=0)
    else:
        start = now + timedelta(hours=1)

    end = start + timedelta(hours=1)

    return start, end


# 🎯 MAIN AGENT
def run_agent(query: str):

    # city detection
    city = extract_city(query)

    # real weather
    temp, wind = get_weather(city)

    # decision
    decision, reason = meeting_decision(temp, wind)

    # priority
    priority = get_priority(query)

    # scheduling
    start, end = get_meeting_time()

    # calendar event
    try:
        link = create_event(
            summary=f"Sales Meeting - {city}",
            start_time=start.isoformat(),
            end_time=end.isoformat()
        )
    except Exception as e:
        print("Calendar Error:", e)
        link = "#"

    # response
    return {
        "city": city,
        "temp": temp,
        "wind": wind,
        "decision": decision,
        "reason": reason,
        "time": start.strftime('%I %p'),
        "priority": priority,
        "link": link
    }
