def find_common_participants(participants_first, participants_second, separator=','):
    first_set = set(participants_first.split(separator))
    second_set = set(participants_second.split(separator))
    common_participants = list(first_set.intersection(second_set))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)