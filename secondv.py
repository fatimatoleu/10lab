"""
Реализуйте функцию, которая выполняет операции над двумя
матрицами (сложение, вычитание, умножение). Функция принимает
две матрицы и символ операции, а возвращает результат операции. 
Используйте функции enumerate(), zip() и len()
"""
def matrix_operation(matrix1, matrix2, operator):
    """
    Функция, которая выполняет операции над двумя матрицами (сложение, вычитание, умножение)
    
    Аргументы:
    matrix1 (list[list]): первая матрица
    matrix2 (list[list]): вторая матрица
    operator (str): символ операции ('+', '-', '*')
    
    Возвращает:
    list[list]: результат операции над двумя матрицами
    """
    # Проверка на возможность выполнения операции
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы имеют разные размеры")

    # Инициализация результирующей матрицы
    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Выполнение операции в зависимости от заданного оператора
    for i, row in enumerate(matrix1):
        for j, elem in enumerate(row):
            if operator == '+':
                result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            elif operator == '-':
                result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
            elif operator == '*':
                # Использование функции zip() и распаковки кортежа
                result_matrix[i][j] = sum(a * b for a, b in zip(matrix1[i], [row[j] for row in matrix2]))

    return result_matrix
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Матрица 1:")
for row in matrix1:
    print(row)

print("Матрица 2:")
for row in matrix2:
    print(row)

print("Результат сложения матриц:")
print(matrix_operation(matrix1, matrix2, '+'))

print("Результат вычитания матриц:")
print(matrix_operation(matrix1, matrix2, '-'))

print("Результат умножения матриц:")
print(matrix_operation(matrix1, matrix2, '*'))
