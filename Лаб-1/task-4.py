users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
all_visits = len(users)
unique_visiter = len(set(users))
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict_users = {
    "Общее количество": all_visits,
    "Уникальные посещения": unique_visiter
    }
print(dict_users)