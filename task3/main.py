import argparse
from process_data import load_logs, parse_log_line, filter_logs_by_level, count_logs_by_level, display_log_counts, display_log_level_details

# python3 task3/main.py task3/log.txt --log-level=error
def main():
    full_log = []
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the log file")
    parser.add_argument("--log-level", default=None, help="Logging level")
    args = parser.parse_args()

    file_path = args.file_path
    log_level = args.log_level

    log_lines = load_logs(file_path)
    if len(log_lines) == 0:
        print("No log")
        return
    
    for log_line in log_lines:
        full_log.append(parse_log_line(log_line))
    logs_counts = count_logs_by_level(full_log)
    display_log_counts(logs_counts)
    if (log_level):
        filtered_log = filter_logs_by_level(full_log, log_level)
        display_log_level_details(filtered_log)


if __name__ == "__main__":
    main()