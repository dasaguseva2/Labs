list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

count = len(list_players)//2

comOne = list_players[:count]
comTwo = list_players[count:]
print(comOne)
print(comTwo)
