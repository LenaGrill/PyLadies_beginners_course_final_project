from random import randrange

def initial_map(n_rows, n_columns):
     """creates a list of lists with n_columns items and n_rows rows """
     clear_map = []
     for _ in range(n_rows):
         clear_map.append(["."] * n_columns)
     return clear_map

def new_map(input_map, coordinates):
    """replaces specific "." positions in the map by "X" """
    draw_map = list(input_map)
    for x, y in coordinates:
        # print(x, y)       
        draw_map[x][y] = "X"
    return draw_map, coordinates

def movement(coordinates, direction, draw_map, n_rows, n_columns):
    i = coordinates[-1][0]
    j = coordinates[-1][1]
    if direction == "n":
        i -= 1
    elif direction == "s":
        i += 1
    elif direction == "e":
        j += 1
    elif direction =="w":
        j -= 1
    elif direction == "end":
        print("Thanks for playing snake! Good bye!")
        return False

    if [i, j] in coordinates: # snake is not allowed to move to a position that is occupied
        return coordinates
    elif not 0 <= i: # snake can't move out of map north
        return coordinates
    elif not i <= n_rows -1 : # snake can't move out of map south
        return coordinates
    elif not 0 <= j: # snake can't move out of map west
        return coordinates
    elif not j <= n_columns -1 : # snake can't move out of map east
        return coordinates
    else:
        coordinates.append([i, j]) # one x is added on the head side of the snake list
        oldest_coordinate = coordinates[0]
        if draw_map[i][j] == "O":
            draw_map = snakefood(draw_map, n_rows, n_columns) # new snakefood is only added, when old one is eaten
            return coordinates
        else:
            draw_map[oldest_coordinate[0]][oldest_coordinate[1]] = "." # x is removed on the map
            coordinates.remove(coordinates[0]) # one x is removed on the tail side of the snake list
            return coordinates

def snakefood(draw_map, n_rows, n_columns):
    while True:
        snakefood_row = randrange(0, n_rows)
        snakefood_column = randrange(0, n_columns)
        print(snakefood_row, snakefood_column)
        if draw_map[snakefood_row][snakefood_column] == ".":
            draw_map[snakefood_row][snakefood_column] = "O"
            return draw_map

def map(n_rows, n_columns):
    a = initial_map(n_rows, n_columns) # empty map is called
    coordinates = [[0,0],[0,1],[0,2]] # these are the starting coordinates for the snake
    draw_map, coordinates = new_map(a, coordinates)
    draw_map = snakefood(draw_map, n_rows, n_columns) # fist snakefood should be already in the map, therefore new_map and snakefood have to be called before while loop
    while True:
        draw_map, coordinates = new_map(a, coordinates) 
        # List the table new_map:
        for row in draw_map:
            for number in row:
                print(number, end = "")
            print()
        direction = input("Please select a movement direction: north = n, east = e, south = s, west = w. End the game = end. ")
        c = movement(coordinates, direction, draw_map, n_rows, n_columns)
        if not c:
            break
        
map(10, 10)



