import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print(hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print(line)
print(zeros)
print(unknown_table)
print(identity)

print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2-5:", hours[2:6])
print("Каждый второй:", hours[::2])
print("В обратном порядке:", hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\nЗадание 3")
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("Центральный фрагмент 2x2:")
center = temperatures[0:2, 1:3]
print(center)
print("shape:", center.shape)

matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
part = matrix[:3]
print("Первые три строки:")
print(part)
print("shape:", part.shape)

part = matrix[:, -2:]
print("Последние два столбца:")
print(part)
print("shape:", part.shape)

part = matrix[:, :2]
print("Первые два столбца:")
print(part)
print("shape:", part.shape)

part = matrix[1:4, 2:5]
print("Строки 1-3, столбцы 2-4:")
print(part)
print("shape:", part.shape)

part = matrix[-2:, -2:]
print("Угловой блок 2x2 справа внизу:")
print(part)
print("shape:", part.shape)


print("\nЗадание 5")


vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print(vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print(small_matrix)


changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("hours:", hours)


changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100  
print("changed_matrix:")
print(changed_matrix)
print("matrix:")
print(matrix)

print("\nЗадание 6")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("numbers:", numbers.shape)
print("table:", table.shape)
print("transposed:", transposed.shape)