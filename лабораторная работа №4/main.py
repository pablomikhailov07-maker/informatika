# TODO импортировать необходимые молули
import csv # импортируем csv
import json  # импортируем json
INPUT_FILENAME = "input.csv" #этот файл мы будем читать
OUTPUT_FILENAME = "output.json" #а в этот файл сохранять


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:  # TODO считать содержимое csv файла# открываем и читаем CSV файл
        y = csv.DictReader(csv_file) #этим действием превращаем строки в словари
        k = list(y)# преобразуем в список
    with open(OUTPUT_FILENAME, 'w', encoding ='utf-8') as json_file:# открываем файл JSON
        json.dump(k, json_file, indent=4, ensure_ascii=False)  # TODO Сериализовать в файл с отступами равными 4
# преобразуем список k, сохраняя запись с отступами, indent=4 – добавляет отступы по 4 пробела для читаемости
if __name__ == '__main__':# проверка работы программы, запущен ли скрипт напрямую
    task() #запуск конвертации
    with open(OUTPUT_FILENAME) as output_f: #открываем созданый для чтения
        for line in output_f:#построчно читаем и выводим json файл
            print(line, end="") #выводим ответ на печать