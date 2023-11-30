from random import randint

commands_for_x = {
    0: 'Значение X - верное',
    1: 'Немного уменьшить X',
    2: 'Уменьшить X',
    3: 'Немного увеличить X',
    4: 'Увеличить X'
}
commands_for_y = {
    0: 'Значение Y - верное',
    1: 'Немного уменьшить Y',
    2: 'Уменьшить Y',
    3: 'Немного увеличить Y',
    4: 'Увеличить Y'
}
point = [randint(-10, 30),randint(2, 28)]
print(f'({point[0]},{point[1]})')

user_point = [None,None]
trys = 0

while trys<8 and user_point != point:
    trys += 1
    print(f'\nПопытка №{trys}:')
    if user_point[0] != point[0]:

        newx = int(input("\nВведите координату X от -10 до 30: "))
        if -10 <= newx <= 30:
            user_point[0] = newx
            if user_point[0] - point[0] == 0:
                print('X угадан.')
            elif 3 > user_point[0] - point[0] > 0:
                print(commands_for_x[1])
            elif user_point[0] - point[0] > 0:
                print(commands_for_x[2])
            elif -3 < user_point[0] - point[0] < 0:
                print(commands_for_x[3])
            elif user_point[0] - point[0] < 0:
                print(commands_for_x[4])
        else:
            print('Введенная координата вне диапазона.')
    else:
        print('X угадан.\n')
    if user_point[1] != point[1]:
        newy = int(input("\nВведите координату Y от 2 до 28: "))
        if 2 <= newy <= 28:
            user_point[1] = newy
            if user_point[1] - point[1] == 0:
                print('Y угадан.')
            elif 3 > user_point[1] - point[1] > 0:
                print(commands_for_y[1])
            elif user_point[1] - point[1] > 0:
                print(commands_for_y[2])
            elif -3 < user_point[1] - point[1] < 0:
                print(commands_for_y[3])
            elif user_point[1] - point[1] < 0:
                print(commands_for_y[4])
        else:
            print('Введенная координата вне диапазона.')
    else:
        print('Y угадан.\n')
if user_point == point:
    print('\nПоздравляю!!! Вы угадали менее чем за 8 попыток.')
else:
    print('\nК сожалению, у вас кончились попытки.')
