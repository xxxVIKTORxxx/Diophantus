y_min = 5
y_max = 10

y_list = []

for y in range(10):
    if y >= y_min and y <=y_max:
        y_list.append(y)

print(y_list)


def equastion(mult_x, mult_y, y_list, result):
    x_list = []
    for y in y_list:
        x = ( result - (mult_y*y) ) / mult_x
        #if x % 1:
        #    pass
       # else:
        x_list.append(x)
    
    return x_list

# 5x+3y=22
print( equastion(5, 3, y_list, 22) )
