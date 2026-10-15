def analyze_results(data):
    # 1. Собираем все команды
    teams = set()
    for race in data:
        teams.update(race.keys())
    teams = sorted(teams)

    # 2. Печатаем список команд
    print('Команды, участвовавшие в чемпионате:')
    for team in teams:
        print(team)

    # 3. Считаем очки по всем гонкам
    scores = {}
    for team in teams:
        total = 0
        for race in data:
            total += race.get(team, 0)
        scores[team] = total

    # 4. Находим победителя
    winner = max(scores, key=scores.get)

    # 5. Без пустой строки — сразу выводим победителя
    print(f'В чемпионате победила команда {winner} с результатом {scores[winner]} баллов')