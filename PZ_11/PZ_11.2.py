#2. Из предложенного текстового файла (text18.9.txt) вывести на экран его содержимое, количество букв
#в нижнем регистре. Сформировать новый файл, в который поместить текст в стихотворной
#форме предварительно поставив последнюю строку фразой введенной пользователем.
file18 = open('PZ11/text18-9 (1).txt', 'r')
text = file18.read()
lower_case = sum(1 for char in text if char.islower())
print('Содержимое файла:', '\n' + text,
      '\nКоличество букв в нижнем регистре:', lower_case)
file18.close()

new_file = open('PZ11/new_file1.txt', 'w')
text = 'И молвил он, сверкнув очами: \n«Ребята! не Москва ль за нами? \nУмремте же под Москвой, \nКак наши братья умирали!» \nИ умереть мы обещали, \nИ клятву верности сдержали' '\n'
new_file.write(text)
razdelenie = text.split('\n')
print(text)
vvod = input("Введите последнюю сторочку (Мы в Бородинский бой.): ")
if vvod == 'Мы в Бородинский бой' or vvod == 'Мы в бородинский бой' or  vvod == 'мы в бородинский бой' or vvod == 'мы в Бородинский бой':
      print(text + vvod)
else:
      print("Введите правильную строчку")
for el in razdelenie[:-1]:
      elem = el + '\n'
      new_file.write(elem)
      new_file.write(vvod)
new_file.close()





