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