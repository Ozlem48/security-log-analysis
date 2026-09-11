import win32evtlog

server = 'localhost'
log_type = 'Security'

hand = win32evtlog.OpenEventLog(server, log_type)

flags = (
    win32evtlog.EVENTLOG_BACKWARDS_READ
    | win32evtlog.EVENTLOG_SEQUENTIAL_READ
)

events = win32evtlog.ReadEventLog(hand, flags, 0)

logs = []

for event in events:

    event_id = event.EventID

    if event_id in [4624, 4625]:

        log = {
            "event_id": event_id,
            "time": event.TimeGenerated,
            "data": event.StringInserts
        }

        logs.append(log)

win32evtlog.CloseEventLog(hand)

for log in logs:
    print(log)