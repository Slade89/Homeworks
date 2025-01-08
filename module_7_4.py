team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

# Использование %:
print('В команде Мастера кода участников: %(number)s!' % {'number': team1_num})
print('Итого сегодня в командах участников: %(number_1)s и %(number_2)s!''\n'
    % {'number_1': team1_num, 'number_2': team2_num}, end='')

# Использование format():
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}!'.format(team1_time))

# Использование f-строк:
print (f'Команды решили {score_1} и {score_2} задач.')

#challenge_result:

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')

#tasks_total и time_avg:

tasks_total = sum([score_1, score_2])
time_avg = sum([team1_time, team2_time]) / 2

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
