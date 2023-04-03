"""
Реализуйте функцию для решения задачи о рюкзаке с помощью
динамического программирования. Функция принимает два списка
(веса и стоимости предметов) и максимальный вес рюкзака, а
возвращает максимальную стоимость, которую можно унести в
рюкзаке. Используйте функции range(), enumerate() и max()
"""
def knapsack(weights, values, max_weight):
    """
    Функция, которая решает задачу о рюкзаке с помощью динамического программирования.
    
    Аргументы:
    weights (list): список весов предметов
    values (list): список стоимостей предметов
    max_weight (int): максимальный вес рюкзака
    
    Возвращает:
    int: максимальная стоимость, которую можно унести в рюкзаке
    """
    # Инициализация двумерного списка для хранения максимальной стоимости
    # в рюкзаке для каждой комбинации предметов и веса рюкзака
    dp_table = [[0 for _ in range(max_weight + 1)] for _ in range(len(weights) + 1)]

    # Заполнение dp_table
    for i in range(1, len(weights) + 1):
        for j in range(1, max_weight + 1):
            if weights[i - 1] <= j:
                dp_table[i][j] = max(values[i - 1] + dp_table[i - 1][j - weights[i - 1]], dp_table[i - 1][j])
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    return dp_table[-1][-1]
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
max_weight = 7

print(knapsack(weights, values, max_weight))  # Output: 9
