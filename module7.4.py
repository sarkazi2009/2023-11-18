
team1_num = 5  # команда мастера кода
team2_num = 6  # команда Волшебника кода
score_1 = 40  #количества задач решенных мастерами кода
score_2 = 42  #количества задач решенных Волшебниками кода
team1_time = 1552.512  #время решения задач мастерами кода
team2_time = 2153.31451  #время решения задач Волшебниками кода
tasks_total = 82  #количество задач
time_avg = 45.2  #среднее время решения задач
challenge_result = 'Победа команды Волшебники данных!'
print("В команде Мастера кода участников: %s ! " % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print(f'Волшебники данных решили задачи за {team1_time} с !')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
