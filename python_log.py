import win32evtlog
import pandas as pd

server = 'localhost'
log_type = 'Security'

hand = win32evtlog.OpenEventLog(server, log_type)

flags = (
    win32evtlog.EVENTLOG_BACKWARDS_READ
    | win32evtlog.EVENTLOG_SEQUENTIAL_READ
)

events = win32evtlog.ReadEventLog(hand, flags, 0)

logs = []
print("Okunan event sayısı:", len(events))

for event in events:

    event_id = event.EventID
    print("Event ID:", event_id)

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
    
    
df = pd.DataFrame(logs)

print("\nDataFrame:")
print(df)

df = pd.read_csv("dataset.csv")

df.columns = [
    "timestamp",
    "source",
    "event_id",
    "task_category",
    "description"
]
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    format="%d.%m.%Y. %H:%M:%S"
)

print(df.head())
print(df.dtypes)

print(df["event_id"].value_counts())