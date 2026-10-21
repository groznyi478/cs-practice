import sys
from logstats import parse_event, count_levels, top_errors, format_report


def main():
    
    log_filename = sys.stdin.readline().strip()
    if not log_filename:
        return

    total_lines = 0
    error_lines = 0
    broken_lines = 0


    with open(log_filename, "r", encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue
            total_lines += 1
            try:
                event = parse_event(line)
                if event["level"] == "ERROR":
                    error_lines += 1
            except ValueError:
                broken_lines += 1


    print(total_lines)
    print(error_lines)
    print(broken_lines)


    with open(log_filename, "r", encoding="utf-8") as log:
        all_lines = log.readlines()

    counts = count_levels(all_lines)
    top_errs = top_errors(all_lines, 3)  # Нам нужны топ-3 частых ошибок по примеру
    report_text = format_report(counts, top_errs)


    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)


if __name__ == "__main__":
    main()