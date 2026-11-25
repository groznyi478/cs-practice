import numpy as np

def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int,
              column_start: int, column_stop: int) -> list[list[float]]:
    a = np.array(matrix)
    return a[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int,
                      column_start: int, column_stop: int,
                      value: float) -> list[list[float]]:
    a = np.array(matrix).copy()
    a[row_start:row_stop, column_start:column_stop] = value
    return a.tolist()

def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return (np.array(matrix) @ np.array(vector)).tolist()

def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return (np.array(left) @ np.array(right)).tolist()

def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return np.array(matrix).T.tolist()

def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    x = np.linalg.solve(np.array(matrix), np.array(vector))
    return [round(float(v), 6) for v in x]

def _mean_last_axis(t):
    if isinstance(t[0], (list, tuple)):
        return [_mean_last_axis(item) for item in t]
    return float(np.mean(t))

def tensor_channel_mean(tensor: list) -> list:
    try:
        return np.array(tensor).mean(axis=-1).tolist()
    except ValueError:
        return _mean_last_axis(tensor)

def point_distance(first: list[float], second: list[float]) -> float:
    d = np.linalg.norm(np.array(first) - np.array(second))
    return round(float(d), 6)