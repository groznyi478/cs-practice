def parse_record(line: str) -> dict:
    fields = [part.strip() for part in line.strip().split(";")]

    if len(fields) != 3:
        raise ValueError("Ожидаются три поля: город;температура;дата")

    city, temperature_text, date = fields

    if not city:
        raise ValueError("Название города не может быть пустым")

    if not date:
        raise ValueError("Дата не может быть пустой")

    try:
        temperature = float(temperature_text)
    except ValueError as exc:
        raise ValueError("Температура должна быть числом") from exc

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }
def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records
def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0.0) + temperature
        counts[city] = counts.get(city, 0) + 1

    return {
        city: round(totals[city] / counts[city], 1)
        for city in totals
    }


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        raise ValueError("Нет корректных записей для определения города")

    return min(averages, key=lambda city: (-averages[city], city))