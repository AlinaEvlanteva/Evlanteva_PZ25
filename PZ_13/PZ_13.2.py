#В матрице найти среднее арифметическое положительных элементов, кратных 3
from functools import reduce
import random
print("Исходная матрица:")
matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
for row in matrix:
    print(row)
def function (matrix):
    martix_in_spisok = [element for row in matrix for element in row]
    filtered_elements = filter(lambda x: x > 0 and x % 3 == 0,  martix_in_spisok)
    filtered_elements_list = list(filtered_elements)
    sum_filtered = reduce(lambda x, y: x + y, filtered_elements_list)
    count_filtered = len(filtered_elements_list)
    return sum_filtered / count_filtered


print('Среднее арифметическое:', function(matrix))





#     count = 0
#     sum = 0
#     for element in filtered_elements:
#         count += 1
#         sum += element
#     if count > 0:
#         return sum / count
#     else:
#         return 0
# print("Среднее арифметическое:", function(matrix))

