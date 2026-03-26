
from datetime import datetime, timedelta
from calendar_utils import create_event

def run_agent(query: str):
    city = "Bangalore"
    if "in" in query:
        city = query.split("in")[-1].strip().title()

    start = datetime.now() + timedelta(hours=1)
    end = start + timedelta(hours=1)

    link = create_event(
        summary=f"Sales Meeting - {city}",
        start_time=start.isoformat(),
        end_time=end.isoformat()
    )

    return f"Meeting scheduled in {city} at {start.strftime('%I %p')} | Link: {link}"
