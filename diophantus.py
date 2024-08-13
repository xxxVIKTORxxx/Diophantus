
def equastion(y_min, y_max, mult_x, mult_y, result):
    y_list = []
    for y in range(y_max):
        if y >= y_min and y <=y_max:
            y_list.append(y)

    x_list = []
    for y in y_list:
        x = ( result - (mult_y*y) ) / mult_x
        #if x % 1:
        #    pass
       # else:
        x_list.append(x)
    
    return x_list

# 5x+3y=22
print( equastion(5, 10, 5, 3, 22) )
