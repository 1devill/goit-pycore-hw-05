from collections import Counter

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print("File was not found, please provide correct file path")
        return []

def parse_log_line(line: str) -> dict:
    date, time, level, *message_parts = line.split(" ")
    full_msg = " ".join(message_parts).strip()
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": full_msg
    }

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if level.lower() == log["level"].lower()]

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log["level"] for log in logs))

def display_log_counts(counts: dict):
    LOG_LEVEL_SPACES = 9
    COUNT_SPACES = 5
    print("\nLog level | Count")
    print("--------- | -----")
    for key, value in counts.items():
        print(f"{key}{' ' * (LOG_LEVEL_SPACES - len(key))} | {value}{' ' * (COUNT_SPACES - len(str(value)))}")

    print("\n")

def display_log_level_details(logs: list[dict]):
    if len(logs) == 0:
        print("No logs for this level")
        return
    
    print(f"Log details for level '{logs[0]["level"]}'")
    for log in logs:
        print(f"{log["date"]} {log["time"]} - {log["message"]}")