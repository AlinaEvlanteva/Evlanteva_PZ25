#2. Арифметические действия над числами пронумерованы следующим образом:
# 1-сложение,2-вычитание, 3-умножение, 4-деление.
# Дан номер действия N (целое число в диапазоне 1.-4) и вещественные числа A и B (B не равно 0).
# Выполнить над числами указанное действие и вывести результат.
try:
    A = float(input("Введите число A: "))
    B = float(input("Введите число B: "))
    if B == 0:
        print("Проверьте правильность введёных данных! B: не должно быть = 0.")
        exit()
    N = int(input("Введите номер действия в диапазоне от 1 до 4.(1-сложение,2-вычитание, 3-умножение, 4-деление): "))
    if N <= 0 or N > 4:
        print("Проверьте правильность введёных данных  N: должен быть в диапозоне от 1 до 4")
    if N == 1:
        print("Результат сложения: ", A + B)
    elif N == 2:
        print("Результат вычитания: ", A - B)
    elif N == 3:
        print("Результат умножения: ", A * B)
    elif N == 4:
        print("Результат деления: ", A / B)
except ValueError:
    print("Проверьте правильность введёных данных!")




