from icalendar import Calendar
from datetime import datetime

def split_ical_by_event(file_path):
    with open(file_path, 'r') as file:
        ical_content = file.read()

    result = Calendar().from_ical(ical_content)
    return result

def format_event_date(event_date):
    if isinstance(event_date, datetime):
        return event_date.strftime('%Y-%m-%d %H:%M:%S')
    return str(event_date)


ical_file = 'icalexport.ics'  

events = split_ical_by_event(ical_file)


for event in events.walk(name="VEVENT"):
    summary = event.get("SUMMARY")
    dtend = format_event_date(event.get("DTEND").dt)
    
    print(f"{dtend}: {summary}")
    print()