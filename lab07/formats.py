import json
import re


def csv_to_records(text: str) -> list[dict]:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    records = []
    for ln in lines[1:]:
        values = [v.strip() for v in ln.split(",")]
        records.append(dict(zip(header, values)))
    return records


_INT = re.compile(r"[+-]?\d+")
_FLOAT = re.compile(r"[+-]?\d+\.\d+")


def _convert(value: str):
    value = value.strip()
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if _INT.fullmatch(value):
        return int(value)
    if _FLOAT.fullmatch(value):
        return float(value)
    return value