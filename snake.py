# def initial_map(x_axis, y_axis):
    # """creates a list of lists with x_axis items and y-axis rows;
    #    the method seems to be correct and the resulting list is fine, 
    #    but cannot be used, as the replacement of dot by X doesn't work properly"""
    # row = []
    # clear_map = []
    # for positions in range(x_axis):
    #     row.append(".")
    # # print(row)
    # for lines in range(y_axis):
    #     clear_map.append(row)
    # return clear_map

def initial_map(n_rows, n_columns):
     """creates a list of lists with n_columns items and n_rows rows
     """
     clear_map = []
     for _ in range(n_rows):
         clear_map.append(["."] * n_columns)
     return clear_map

# initial_map(10, 10)

# a = [
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","."]]  

def new_map(input_map, coordinates):
    """replaces specific "." positions in the map by "X" """
    draw_map = list(input_map) # I was hoping to not overwrite the initial map a by using list, but somehow, it is always overwritten
    # print(draw_map)
    # print(a)
    # print(coordinates)
    for x, y in coordinates:

        # print(x, y)       
        draw_map[x][y] = "X"
       
    return draw_map, coordinates


def movement(coordinates, direction):

    i = coordinates[-1][0]
    j = coordinates[-1][1]
    # print(i, j)
    if direction == "n":
        i -= 1
    elif direction == "s":
        i += 1
    elif direction == "e":
        j += 1
    elif direction =="w":
        j -= 1
    # print(i, j)
    elif direction == "end":
        print("Thanks for playing snake! Good bye!")
        return False

    coordinates.append([i, j])
    # print(coordinates[0])
    oldest_coordinate = coordinates[0]
    print(oldest_coordinate)
    coordinates.remove(coordinates[0]) # first try to remove X at the end of the snake. Works for the list, not for the map.
                                        # the initial map is overwritten, so does the X have to be overwritten again by dots?
    print("snake position: ", coordinates)
    return coordinates

def map():
    a = initial_map(10, 10)
    # print(a)
    
    # List the table clear_map:
    for row in a:
        for number in row:
            print(number, end = "")
        print()
    coordinates = [[0,0],[0,1],[0,2]]
    while True:
        print(a)
        draw_map, coordinates = new_map(list(a), coordinates) 
        # a alone overwrites a, so I am trying to get a new list with list(a), but that doesn't work either
        # why is a overwritten by draw_map???
        # print(draw_map)
        print(a)
        # List the table new_map:
        for row in draw_map:
            for number in row:
                print(number, end = "")
            print()

        direction = input("Please select a movement direction: north = n, east = e, south = s, west = w. End the game = end. ")
    
        c = movement(coordinates, direction)
        # print(a)
        if not c:
            break
        

map()



