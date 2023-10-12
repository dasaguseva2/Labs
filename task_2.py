# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, n=','):
    first_group = participants_first.split(n)
    second_group = participants_second.split(n)
    group = []
    for i in first_group:
        for j in second_group:
            if i == j:
                group.append(i)
    return group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))