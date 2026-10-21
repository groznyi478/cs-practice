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