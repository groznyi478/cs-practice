LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line):
    pass


def count_levels(lines):
    pass


def top_errors(lines, n):
    pass


def format_report(counts, errors):
    pass
def parse_event(line):
    parts = line.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"Неверная строка: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"Неизвестный уровень: {level!r}")
    return {"time": time, "level": level, "message": message.strip()}
def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts
def top_errors(lines, n):
    freq = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            freq[msg] = freq.get(msg, 0) + 1
    ordered = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return [[msg, count] for msg, count in ordered[:n]]