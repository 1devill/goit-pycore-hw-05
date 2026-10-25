import argparse
from process_data import (
    load_logs,
    parse_log_line,
    filter_logs_by_level,
    count_logs_by_level,
    display_log_counts,
    display_log_level_details,
)

# Usage:
#   python3 task3/main.py task3/log.txt
#   python3 task3/main.py task3/log.txt error


def main():
    parser = argparse.ArgumentParser(description="Analyze a log file")
    parser.add_argument("file_path", help="Path to the log file")
    parser.add_argument("log_level", nargs="?", default=None,
                        help="Optional log level to show details for (e.g. error)")
    args = parser.parse_args()

    log_lines = load_logs(args.file_path)
    if not log_lines:
        print("No logs to analyze.")
        return

    logs = []
    skipped = 0
    for line_number, line in enumerate(log_lines, start=1):
        if not line.strip():
            continue
        parsed = parse_log_line(line)
        if parsed is None:
            skipped += 1
            print(f"Warning: skipped malformed line {line_number}: {line.strip()}")
            continue
        logs.append(parsed)

    if not logs:
        print("No valid log entries found.")
        return

    display_log_counts(count_logs_by_level(logs))
    if skipped:
        print(f"Skipped malformed lines: {skipped}\n")

    if args.log_level:
        filtered = filter_logs_by_level(logs, args.log_level)
        display_log_level_details(filtered, args.log_level)


if __name__ == "__main__":
    main()
