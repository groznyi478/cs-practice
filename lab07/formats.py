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
    if value in ("true", "yes"):
        return True
    if value in ("false", "no"):
        return False
    if _INT.fullmatch(value):
        return int(value)
    if _FLOAT.fullmatch(value):
        return float(value)
    return value

def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None
    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("- ") or line == "-":
            if current_list is not None:
                result[current_list].append(_convert(line[1:]))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value == "":
            result[key] = []
            current_list = key
        else:
            result[key] = _convert(value)
            current_list = None
    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged = []
    for row in rows:
        info = extra.get(row.get(key), {})
        merged.append({**info, **row})
    return merged

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)