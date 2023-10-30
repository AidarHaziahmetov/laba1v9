min_x = -10
max_x = 30
min_y = 2
max_y = 28
def binnary_searcing(min_coord,max_coord,searcing_coord, count_of_trys=0):
    global min_x 
    global max_x
    global min_y
    global max_y
    count_of_trys += 1
    coord = min_coord+ (max_coord - min_coord)//2
    if coord == searcing_coord:
        return [coord, count_of_trys]
    elif coord < searcing_coord:
        if searcing_coord  - coord < 3:
            return binnary_searcing(coord+1, coord+2, searcing_coord, count_of_trys)
        else:
            return binnary_searcing(coord+1, max_coord, searcing_coord, count_of_trys)
    elif coord > searcing_coord:
        if coord - searcing_coord < 3:
            return binnary_searcing(coord-2, coord-1, searcing_coord, count_of_trys)
        else:
            return binnary_searcing(min_coord, coord-1, searcing_coord, count_of_trys)

print(binnary_searcing(2,28,0))

def binnary_searcing_point(x,y):
    global min_x 
    global max_x
    global min_y
    global max_y