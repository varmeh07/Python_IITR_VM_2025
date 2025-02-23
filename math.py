def sqr_rt(num):
    left=0
    right=num
    while True:
        mid = (left+right)/2
        result = mid*mid
        diff = abs(result - num)
        if diff <=0.0001:
            return mid
            print(mid)
        else:
            if result > num:
                right = mid
            else:
                left = mid

def cube_rt(num):
    left=0
    right=num
    while True:
        mid = (left+right)/2
        result = mid*mid*mid
        diff = abs(result - num)
        if diff <=0.0001:
            return mid
            print(mid)
        else:
            if result > num:
                right = mid
            else:
                left = mid

def hypot(x,y):
    c=sqr_rt(x*x+y*y)
    return c

def is_in_rectangle(x1,x2,y1,y2,a,b):
    z1=a
    z2=b
    print(x1,x2,y1,y2,a,b)
    #if (z1 in range(x1,x2,1) and z2 in range(y1,y2,1)):
    if (x1<=a and a<=x2 and y1<=b and b<=y2):
        return True
    else: 
        return False

if __name__ == '__main__':
    num=125
    x,y=1,2
    a,b=1,5
    sqrt=sqr_rt(num)
    print(f"square root of {num} = {sqrt}",)
    cubrt=cube_rt(num)
    print(f"cube root of {num} = {cubrt}",)
    hypotenus=hypot(x,y)
    print(f"the hypotenus of {x} and {y} = {hypotenus}",)
    distance_2d=hypot(x-a,y-b)
    print(f"the distnace in 2d is = {distance_2d}",)
    
    '''
        rectangle overlaping
    '''
    rectangle2=[1,3,1,3]
    rectangle1=[2,4,2,4]
    i=0
    flag=False
    #g=2
    for i in range(2):
        j=2
        while j<4:
            if is_in_rectangle(rectangle1[0],rectangle1[1],rectangle1[2],rectangle1[3],rectangle2[i],rectangle2[j]):
                print(i,j)
                print('Overlapping')
                flag=True
                break
            else:
                #print(i,j)
                print('Not Overlapping')
            j+=1

    i+=1
    if(flag):
        print("the rectangle coordinates are overlapping")
    else:
        print("no overlapping try another set")
