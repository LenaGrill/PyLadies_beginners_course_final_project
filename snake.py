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

# def initial_map(x_axis, y_axis):
#     """not finished yet! creates a list of lists with x_axis items and y-axis rows"""

#     clear_map = str((".," * x_axis, ";") * y_axis)
#     split_map = clear_map.split(",")
#     print(clear_map)
#     print(split_map)


# initial_map(10, 10)

a = [
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."]]  

def new_map(a, coordinates):
    """replaces specific "." positions in the map by "X" """
    draw_map = a
    # print(draw_map)
    # print(coordinates)
    for x, y in coordinates:

        # print(x, y)       
        draw_map[x][y] = "X"
            
    return draw_map, coordinates


def movement(coordinates, direction):

    i = coordinates[-1][-2]
    j = coordinates[-1][-1]
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
    # coordinates.remove(coordinates[0])
    print("snake position: ", coordinates)
    return coordinates

def map():
    # a = initial_map(10, 10)
    # print(a)
    
    # List the table clear_map:
    # for row in a:
    #     for number in row:
    #         print(number, end = "")
    #     print()
    coordinates = [[0,0],[0,1],[0,2]]
    while True:
        draw_map, coordinates = new_map(a, coordinates)
        # List the table new_map:
        # print(draw_map)
        for row in draw_map:
            for number in row:
                print(number, end = "")
            print()

        direction = input("Please select a movement direction: north = n, east = e, south = s, west = w. ")
    
        c = movement(coordinates, direction)
        if not c:
            break

map()



