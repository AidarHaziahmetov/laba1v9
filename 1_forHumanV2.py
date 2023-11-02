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



def guessing(point, count_of_trys=0):
    
    count_of_trys += 1
    try:    
        user_point = list(map(int,input(f'Попытка {count_of_trys}: Введите X и Y через пробел: ').split()))

        if -10 <=  user_point[0] <= 30 and 2 <= user_point[1] <= 28:
            if user_point == point:
                if count_of_trys <= 8:
                    print(f'Ты молодец! Попыток потрачено: {count_of_trys}.')
                    
                else:
                    print(f'Ты cправился, но потратил слишкомного попыток: {count_of_trys}.')
                print()
                point = [randint(-10, 30),randint(2, 28)]
                guessing(point)

            else:
                if user_point[0] - point[0] == 0:
                    print(commands_for_x[0])
                elif 3 > user_point[0] - point[0] > 0:
                    print(commands_for_x[1])
                elif user_point[0] - point[0] > 0:
                    print(commands_for_x[2])
                elif -3 < user_point[0] - point[0] < 0:
                    print(commands_for_x[3])
                elif user_point[0] - point[0] < 0:
                    print(commands_for_x[4])

                if user_point[1] - point[1] == 0:
                    print(commands_for_y[0])
                elif 3 > user_point[1] - point[1] > 0:
                    print(commands_for_y[1])
                elif user_point[1] - point[1] > 0:
                    print(commands_for_y[2])
                elif -3 < user_point[1] - point[1] < 0:
                    print(commands_for_y[3])
                elif user_point[1] - point[1] < 0:
                    print(commands_for_y[4])
                guessing(point, count_of_trys)
        else:
            print('Неверно заданы координаты')
            guessing(point, count_of_trys-1)

    except ValueError:
        print('Неверно указаны координаты')
        guessing(point, count_of_trys-1)
    except IndexError:
        print('Неверно указаны координаты')
        guessing(point, count_of_trys-1)

guessing(point)