from event_manager import build_report, load_events, sort_events_by_date


def test_sort_events_by_date_earliest_first():
    events = [
        {"title": "Later", "date": "2026-11-20", "venue": "A"},
        {"title": "Earlier", "date": "2026-11-02", "venue": "B"},
    ]

    result = sort_events_by_date(events)

    assert [event["title"] for event in result] == ["Earlier", "Later"]


def test_build_report_contains_event_information():
    events = [
        {"title": "Game Night", "date": "2026-11-12", "venue": "Student Center"}
    ]

    result = build_report(events)

    assert "Game Night" in result
    assert "2026-11-12" in result
    assert "Student Center" in result


def test_load_events_reads_json(tmp_path):
    data_file = tmp_path / "events.json"
    data_file.write_text(
        '[{"title":"Test Event","date":"2026-11-01","venue":"Library"}]',
        encoding="utf-8",
    )

    result = load_events(data_file)

    assert result == [
        {"title": "Test Event", "date": "2026-11-01", "venue": "Library"}
    ]


def test_build_report_handles_missing_title():
    events = [
        {"date": "2026-11-15", "venue": "Library"}
    ]

    result = build_report(events)

    assert "Untitled Event" in result


def test_filter_events_by_venue_is_case_insensitive():
    from event_manager import filter_events_by_venue

    events = [
        {"title": "A", "date": "2026-11-01", "venue": "Student Center"},
        {"title": "B", "date": "2026-11-02", "venue": "Library"},
        {"title": "C", "date": "2026-11-03", "venue": "student center"},
    ]

    result = filter_events_by_venue(events, "STUDENT CENTER")

    assert [event["title"] for event in result] == ["A", "C"]


def test_build_report_can_filter_by_venue():
    events = [
        {"title": "Game Night", "date": "2026-11-12", "venue": "Student Center"},
        {"title": "Movie Night", "date": "2026-11-19", "venue": "Library Auditorium"},
    ]

    result = build_report(events, venue="Student Center")

    assert "Game Night" in result
    assert "Movie Night" not in result
