def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        if "." in name:
            ext = name.rsplit(".", 1)[1].lower()
        else:
            ext = ""                        
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    value = float(n_bytes)
    i = 0
    while (value >= 1024 or round(value, 1) >= 1024) and i < len(units) - 1:
        value /= 1024
        i += 1
    return f"{value:.1f} {units[i]}"