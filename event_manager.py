"""Student Club Event Manager."""

import json


def load_events(filename):
    """Load event records from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def format_event(event):
    """Return one event as a readable line of text."""
    return f"{event['date']} | {event['title']} | {event['venue']}"


def build_report(events):
    """Build a printable event report."""
    lines = ["Student Club Events", "-------------------"]
    for event in events:
        lines.append(format_event(event))
    return "\n".join(lines)


def main():
    events = load_events("events.json")
    print(build_report(events))


if __name__ == "__main__":
    main()
