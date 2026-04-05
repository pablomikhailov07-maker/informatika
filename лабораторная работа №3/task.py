# TODO Напишите функцию find_common_participants

def find_common_participants( g1, g2, delimiter=','): #напишем функцию find_common_participants и укажем разделитель ','
    l1 = g1.split(delimiter)#разделяем строки на участников для первой группы
    l2 = g2.split(delimiter)#разделяем строки на участников для второй группы
    common = set(l1) & set(l2) #найдем общих участников
    return sorted(common) #функция должна возращать список, отсортируем его
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
r = find_common_participants(participants_first_group,participants_second_group, ';') #c помощью этого действия вызовем функцию
# TODO Провеьте работу функции с разделителем отличным от запятой
print(r) #выводим результат на печать