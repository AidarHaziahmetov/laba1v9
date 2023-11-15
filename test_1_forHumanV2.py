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
print(point)


def guessing(point, count_of_trys=0,user_point=None):
    
    count_of_trys += 1
    if count_of_trys == 9:
        return 'У тебя кончились попытки'
    try:
        if user_point == None:
            user_point = list(map(int,input(f'Попытка {count_of_trys}: Введите X и Y через пробел: ').split()))

        if -10 <=  user_point[0] <= 30 and 2 <= user_point[1] <= 28:
            if user_point == point:
                if count_of_trys <= 8:
                    return f'Ты молодец! Попыток потрачено: {count_of_trys}.'
                    
                else:
                    return f'Ты cправился, но потратил слишкомного попыток: {count_of_trys}.'

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
                # return guessing(point, count_of_trys)
        else:
            print('Координаты находятся вне диапазона')
            return guessing(point, count_of_trys)

    except ValueError:
        print('Координаты должны быть числами')
        return  guessing(point, count_of_trys)
    except TypeError:
        print('Координаты должны быть числами')
        return  guessing(point, count_of_trys)
    except IndexError:
        print('Вы ввели только одну координату')
        return guessing(point, count_of_trys)
print(guessing(point))


# def test_win():
#     point = [4,5]
#     user_inputs = [[10,10], [0,0], [5,5], [4,5]]
#     for i in range(len(user_inputs)):
#         test_output =  guessing(point,i,user_inputs[i])
#     assert test_output == 'Ты молодец! Попыток потрачено: 4.'

# def test_try_is_out():
#     point = [4,5]
#     user_inputs = [[10,10], [0,0], [5,5], [5,5], [5,5],[5,5],[5,5],[5,5],[4,5]]
#     for i in range(len(user_inputs)):
#         test_output =  guessing(point,i,user_inputs[i])
#     assert test_output == 'У тебя кончились попытки'

# def test_input_out_of_range():
#     point = [4,5]
#     user_inputs = [[-11,-1]]
#     for i in range(len(user_inputs)):
#         test_output =  guessing(point,i,user_inputs[i])
#     assert test_output == 'Координаты находятся вне диапазона'

# def test_input_is_not_number():
#     point = [4,5]
#     user_inputs = [['b','a']]
#     for i in range(len(user_inputs)):
#         test_output =  guessing(point,i,user_inputs[i])
#     assert test_output == 'Координаты должны быть числами'

# def test_only_one_num_get():
#     point = [4,5]
#     user_inputs = [[1]]
#     for i in range(len(user_inputs)):
#         test_output =  guessing(point,i,user_inputs[i])
#     assert test_output == 'Вы ввели только одну координату'


# test_win()
# test_try_is_out()
# test_input_out_of_range()
# test_input_is_not_number()
# test_only_one_num_get()