list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
quantity_players = len(list_players)
mid_index = int(quantity_players / 2)
# TODO Разделите участников на две команды
first_team = list_players[:mid_index]
second_team = list_players[mid_index:]
print(first_team)
print(second_team)
