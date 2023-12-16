#Дана строка, содержащая полное имя файла. Выделить из этой строки название последнего каталога (без символов "\").
#Если файл содержится ы корневом каталоге, то вывести символ "\".
def extract_last_directory(full_path):
    directories = full_path.split("\\")  # Разделяем строку по символу "\"
    if len(directories) == 1:  # Если только один элемент, значит файл в корневом каталоге
        return "\\"
    else:
        return directories[-2]  # Возвращаем предпоследний элемент, который является названием последнего каталога

# Пример использования
file_path = "C:\\Users\\Username\\Documents\\file.txt"
result = extract_last_directory(file_path)
print(result)  # Output: "Documents"
