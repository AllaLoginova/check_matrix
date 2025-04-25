import sys

def has_adjacent_ones(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                # Проверяем 8 соседей (кроме самой клетки)
                for di in (-1, 0, 1):     # Генерация возможных смещений              
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue  # Пропускаем текущую клетку
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 1: # Фильтрация границ и проверка значения
                            return True  # Нашли соседнюю единицу
    return False  # Нет соседних единиц

# Чтение входных данных
s = sys.stdin.readlines()
lst_in = [list(map(int, line.strip().split())) for line in s]

# Проверка и вывод
print("НЕТ" if has_adjacent_ones(lst_in) else "ДА")
