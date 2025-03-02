def line_pred(x1,y1,x2,y2,x3):
    delta_x=x1-x2
    delta_y=y1-y2
    slope=delta_y/delta_x
    y3=slope*x3
    return y3, slope

print(line_pred(1,5,3,15,4))

#x1,y1=map(float, input("Input x and y coordinates for point 1\n").split(","))
#x2,y2=map(float, input("Input x and y coordinates for point 2\n").split(","))
x1,y1=map(int, input("Input x and y coordinates for point 1\n").split(","))
x2,y2=map(int, input("Input x and y coordinates for point 2\n").split(","))
x=input("Input x coordinates for point 3\n")
y,slp=line_pred(x1,y1,x2,y2,int(x))
print(f"the slope of the line is  = {slp}\n",)
print(f"the y coordinates for new x is = {y}\n", )
print(type(x1))
print(type(y))
