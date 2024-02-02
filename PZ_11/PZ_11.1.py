#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#Исходные данные:
#Количество элементов:
#Индекс максимального элемента:
#Меняем местами первую и последнюю трети:
file_ = open('PZ11/text_.txt', 'w')
num = 5, 10, 11, -7, -10, -4
file_.write(str(num))
file_.close()

file = open('PZ11/text.txt', 'w')
numbers = 5, 10, 11, -7, -10, -4
file.write(str(numbers))
file.close()

file = open('PZ11/text.txt', 'r')
data = file.read()
print('Содержимое текстового файла (исходные данные):', data)
elements = [num for num in data.split(', ')]
count = len(elements)
print('Количество элементов:', count)
print('Индекс максимального элемента (Число 11):', elements.index(max(elements)))
delenie_treti = count // 3
swap = elements[-delenie_treti:] + elements[delenie_treti:-delenie_treti] + elements[:delenie_treti]
print('Меняем местами первую и последнюю трети:', swap)
file.close()




#elements[:delenie_treti], elements[-delenie_treti:] = elements[-delenie_treti:], elements[:delenie_treti]
#print('Меняем местами первую и последнюю трети:', elements)
#swap = elements[0], elements[5] = elements[5], elements[0]
#delenie_treti = elements

#print(elements)s
#for el in file:
    #text = el.split(', ')
    #print(len(el))
#print('Количество элементов в текстовом файле:', len(file.read()))
#max_index = elements.index(max(elements))
#print('Индекс последнего максимального элемента:', max_index)
#element = [el for el in data.split(', ')]
#print(len(element))