#В матрице найти среднее арифметическое положительных элементов, кратных 3
import random
print("Исходная матрица:")
matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
for row in matrix:
    print(row)
def function (matrix):
    martix_in_spisok = [element for row in matrix for element in row]
    filtered_elements = filter(lambda x: x > 0 and x % 3 == 0,  martix_in_spisok)  # Фильтруем положительные элементы, кратные 3
    count = 0 # кол-во чисел
    total = 0 #сумма чисел
    for element in filtered_elements:
        count += 1
        total += element
    if count > 0:
        return total / count
    else:
        return 0
print("Среднее арифметическое:", function(matrix))
