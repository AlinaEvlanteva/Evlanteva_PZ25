#1) Дано целое число N (>0).Найти сумму 1+1/2+1/3+...+1/N

#2) Дано число A (>1).
# Вывести наименьшее из целых чисел K, для которых сумма
# 1+1/2+...+1/K будет больше A,или саму эту сумму.
try:
    N=int(input("Введите целое число"))
    if N<=0:
        print("Число N должно быть больше 0")

except ValueError:
    print("Число N должно быть больше 0")


