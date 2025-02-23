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
