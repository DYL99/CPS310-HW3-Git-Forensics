# Student Club Event Manager

A small command-line tool for viewing upcoming student club events.

## Product Requirements

- Events are loaded from `events.json`.
- Each event displays its date, title, and venue.
- Event reports must show events in **chronological order, earliest event first**.
- A future feature request asks for filtering the report by venue.

## Run

```text
python event_manager.py
```

## Test

```text
python -m pytest -v
```

## Data Notes

Every event must include a date and venue. If a title is missing, the report displays `Untitled Event` so that one incomplete record does not prevent the full report from being displayed.

## Venue Filtering

Reports can optionally be filtered to a single venue by passing a venue name to `build_report()`.
