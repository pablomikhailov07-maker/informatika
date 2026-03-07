list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
polovina = len(list_players) // 2 # считаем количество игроков и делим на два


team_one = list_players[:polovina] #делаем так, чтобы первая команда была из первой половины
team_two= list_players[polovina:] #делаем так, чтобы первая команда была из второй половины

print(team_one)
print(team_two)
