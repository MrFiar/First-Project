import random


data_person = {}
username = 'username'
#username = input('Ведите имя:')

def add_date():
    print('Сперва введите дату')
    data_day = input('Введите день:')
    data_month = input('Введите месяц в двухзначном значении: например 01 , 09, 12 :')
    # data_year = input('Введите год:')
    mass = float(input('Ваш вес в кг: '))
    fulldate =  data_month + '/' + data_day
    data_person[fulldate] = mass
    print(f'Ваш вес {data_month}/{data_day} составлял {mass}, запись завершена')
    print()



print(f'Привет {username}')


def menu_start():
    print('Для добавления даты и веса введите 1')
    print('Для показа данных о пользователе введите 2')
    print('Выйти из программы введите 3')
    print('для добовления тестовых  даннык введите 4')
    a = input()
    if not a.isdigit:
        print('неверный ввод попробуйте еще')
        print()
        menu_start()
    if a == '1':
        add_date()
        print()
        menu_start()
    elif a == '2':
        print('Вот что у нас записано')
        for key_data_person in data_person:
            print(key_data_person, data_person[key_data_person])
        print()
        menu_start()
    elif a == '3':
        return
    elif a == '4':
        for element_test in range(1, 21, 2):
            if element_test <10:
                key_test = '01/0' + str(element_test)
                values_test = random.randint(100, 103)
                data_person[key_test] = values_test
            else:
                key_test = '01/' + str(element_test)
                values_test = random.randint(100, 103)
                data_person[key_test] = values_test
        print('Записано 10 тестовых значений, вы можете их увидеть если введёте 2')
        print()
        menu_start()

    else:
        print("необходммо ввести от 1 до 4 целыми числами, попробуйте еще")
        menu_start()




menu_start()


