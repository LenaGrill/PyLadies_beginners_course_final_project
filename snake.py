def initial_map(x_axis, y_axis):
    """creates a list of lists with x_axis items and y-axis rows"""
    row = []
    clear_map = []
    for positions in range(x_axis):
        row.append(".")
    # print(row)
    for lines in range(y_axis):
        clear_map.append(row)
    return clear_map
   

def new_map(a, coordinates):
    """replaces specific "." positions in the map by "X" """
    draw_map = a
    print(draw_map)
    print(coordinates)
    for x, y in coordinates:
        print(x, y)       
        draw_map[x][y] = "X"
            
    return draw_map

                    


# def movement():



def map():
    a = initial_map(10, 10)
    print(a)
    # List the table clear_map:
    for row in a:
        for number in row:
            print(number, end = "")
        print()

    b = new_map(a, [[0,0],[1,0],[2,2],[4,3],[8,9]])
    # List the table new_map:
    print(b)
    for row in b:
        for number in row:
            print(number, end = "")
        print()
    # print(b)
        
       
    
    # for position in a:
    #     new_map = a[0][0].replace(".", "x")
    #     print(new_map)

map()

