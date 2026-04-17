def detect_connector(meeting_link):

    if "meet.google.com" in meeting_link:
        import meeting_connector.meet_meeting as connector
        return connector

    elif "zoom.us" in meeting_link:
        import meeting_connector.zoom_meeting as connector
        return connector

    elif "teams" in meeting_link:
        import meeting_connector.teams_meeting as connector
        return connector

    else:
        return None


def open_meeting(meeting_link):
    connector = detect_connector(meeting_link)

    if connector:
        connector.open_meeting(meeting_link)
    else:
        print("Unsupported meeting link")


def raise_hand(meeting_link):
    connector = detect_connector(meeting_link)
    connector.raise_hand()


def lower_hand(meeting_link):
    connector = detect_connector(meeting_link)
    connector.lower_hand()


def unmute_mic(meeting_link):
    connector = detect_connector(meeting_link)
    connector.unmute_mic()


def mute_mic(meeting_link):
    connector = detect_connector(meeting_link)
    connector.mute_mic()


def leave_meeting(meeting_link):
    connector = detect_connector(meeting_link)
    connector.leave_meeting()