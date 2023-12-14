from random import randint
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
                print('Немного уменьшить X')
            elif user_point[0] - point[0] > 0:
                print('Уменьшить X')
            elif -3 < user_point[0] - point[0] < 0:
                print('Немного увеличить X')
            elif user_point[0] - point[0] < 0:
                print('Увеличить X')
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
                print('Немного уменьшить Y')
            elif user_point[1] - point[1] > 0:
                print('Уменьшить Y')
            elif -3 < user_point[1] - point[1] < 0:
                print('Немного увеличить Y')
            elif user_point[1] - point[1] < 0:
                print('Увеличить Y')
        else:
            print('Введенная координата вне диапазона.')
    else:
        print('Y угадан.\n')
if user_point == point:
    print('\nПоздравляю!!! Вы угадали менее чем за 8 попыток.')
else:
    print('\nК сожалению, у вас кончились попытки.')
