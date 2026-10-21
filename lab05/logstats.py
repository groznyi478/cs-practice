def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Некорректный формат строки лога")

    return {
        "time": parts[0],
        "level": parts[1],
        "message": parts[2]
    }