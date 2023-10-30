commands = {
    'Уменьшить значение': '0',
    'Немного уменьшить значение': '1',
    'Увеличить значение': '2',
    'Немного увеличить значение': '3',
    'Значение - верное': '4',

}

def binnary_searcing(coord_min, coord_max, name_of_coord):
    
    if name_of_coord == 'X':
        max_value = 30
        min_value = -10
    else:
        max_value = 28
        min_value = 2
    coord = coord_min+(coord_max - coord_min) // 2
    
    print(f'Предположительное значение вашей координаты {name_of_coord}: {coord} \nВыберите действие: ')
    
    for i in commands.keys():
        print(commands[i], i)
    command = input()

    if command == '4':
        return coord

    elif command == '0':
        if coord > min_value:
            return  binnary_searcing(coord_min, coord-1, name_of_coord)
        else:
            return  binnary_searcing(coord_min, coord, name_of_coord)

    elif command == '1':
        if coord-2 > min_value:
            return  binnary_searcing(coord-2, coord-1, name_of_coord)
        else:
            return  binnary_searcing(min_value, coord-1, name_of_coord)

    elif command == '2':
        if coord < max_value:
            return  binnary_searcing(coord+1, coord_max, name_of_coord)
        else:
            return  binnary_searcing(coord, coord_max, name_of_coord)
    
    elif command == '3':
        if coord+2 <= max_value:
            return  binnary_searcing(coord+1, coord+2, name_of_coord)
        else:
            return  binnary_searcing(coord+1, max_value, name_of_coord)
        
    else:
        print("Комманда введена неверно, попробуйте еще раз")
        return binnary_searcing(coord_min, coord_max, name_of_coord)

print(f'Ваша точка :({binnary_searcing(-10, 30, "X")}, {binnary_searcing(2, 28, "Y")})')
