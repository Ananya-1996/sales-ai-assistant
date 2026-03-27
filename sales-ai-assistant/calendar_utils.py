
from googleapiclient.discovery import build
from google.auth import default

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_service():
    creds, _ = default(scopes=SCOPES)
    return build('calendar', 'v3', credentials=creds)


def create_event(summary, start_time, end_time):
    service = get_calendar_service()

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',
        }
    }

    event = service.events().insert(
        calendarId='primary',
        body=event
    ).execute()

    return event.get('htmlLink')
