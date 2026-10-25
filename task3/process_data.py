from collections import Counter
from datetime import datetime


def load_logs(file_path: str) -> list[str]:
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{file_path}' was not found, please provide a correct file path.")
    except (OSError, UnicodeDecodeError) as error:
        print(f"Could not read file '{file_path}': {error}")
    return []


def parse_log_line(line: str) -> dict | None:
    """Parse 'YYYY-MM-DD HH:MM:SS LEVEL message'. Returns None for malformed lines."""
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None

    date, time, level, message = parts
    try:
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None

    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message.strip(),
    }


def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list[dict]) -> dict:
    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: dict):
    print(f"\n{'Log level':<17}| Count")
    print(f"{'-' * 17}|{'-' * 6}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")
    print()


def display_log_level_details(logs: list[dict], level: str):
    if not logs:
        print(f"No logs for level '{level.upper()}'.")
        return

    print(f"Log details for level '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")
