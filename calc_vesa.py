print('hello world')
print('hello world')
print('hello world')
print('hello world')
age = int(input('Ваш возраст: '))
rost = float(input('Ваш рост в см: '))
mymass = float(input('Ваш вес в кг: '))

kkal = int(input('Введите количество калорий за сегодня: '))

data_kkal_ilia = []


def main_enegry():
    result = 665 + 9.6 * mymass + 1.8 * rost - 4.7 * age
    return result


def my_goal(goal):
    global mymass  # mymass = float(input('Ваш вес в кг: '))
    day = 0
    while mymass >= goal:
        activity = 1.2
        diffic = 665 + 9.6 * mymass + 1.8 * rost - 4.7 * age * activity - kkal
        gram_j = 7716 / 1000.
        mass = diffic / gram_j / 1000
        day += 1
        mymass = mymass - mass

    week = day / 7
    print('Ты будешь весить {:.1f} килограм через: {:.1f} недель'.format(goal, week))


data_kkal_ilia = []


def calorii_den_ilia():
    data_kkal_ilia.append(kkal)
    activity = 1.2
    diffic = main_enegry() * activity - kkal
    gram_j = 7716 / 1000
    mass = diffic / gram_j
    mass_week = mass * 7 / 1000
    mass_4week = mass * 28 / 1000
    result = (110 - 80) / mass_week
    print('Сегодня ты похудел на {:.0f} грамм'.format(mass))
    print('За 1 неделю в таком режиме ты сбросишь: {:.1f} кг.'.format(mass_week))
    print('За 4 недели в таком режиме ты сбросишь: {:.1f} кг.'.format(mass_4week))
    # print('Ты будешь весить 80 килограм через: {:.1f} недель - некоректная формула'.format(result))
    goal_input = float(input('Ввести необходимый вес: '))
    my_goal(goal_input)


calorii_den_ilia()




