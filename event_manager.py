"""Student Club Event Manager."""

import json


def load_events(filename):
    """Load event records from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def format_event(event):
    """Return one event as a readable line of text."""
    title = event.get("title", "Untitled Event")
    return f"{event['date']} | {title} | {event['venue']}"


def sort_events_by_date(events):
    """Return events sorted chronologically, earliest first."""
    return sorted(events, key=lambda event: event["date"], reverse=True)


def filter_events_by_venue(events, venue):
    """Return events whose venue matches the requested venue."""
    return [
        event
        for event in events
        if event["venue"].lower() == venue.lower()
    ]


def build_report(events, venue=None):
    """Build a printable event report, optionally filtered by venue."""
    if venue:
        events = filter_events_by_venue(events, venue)

    lines = ["Student Club Events", "-------------------"]
    for event in sort_events_by_date(events):
        lines.append(format_event(event))
    return "\n".join(lines)


def main():
    events = load_events("events.json")
    print(build_report(events))


if __name__ == "__main__":
    main()
