def line_overlap(line1, line2):
    max1=max(line1)
    min1 = min(line1)
    min2=min(line2)
    max2=max(line2)
    if min2<=max1 and min1<=max2:
        print("line overlap")
        result = True
        return result
    else:
        print("line not overlap")
        result = False
        return result

if __name__ == '__main__':

    line1 = [3,4]
    line2 = [1,5]
    result=line_overlap(line1, line2)
    print(result)