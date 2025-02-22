def base_conversion(num):
    base = 8
    d = 0
    i = 0
    while (num != 0):
        x = num % 10
        d = d + (base ** i) * x
        # print(d)
        i = i + 1
        num = num // 10
    print(d)

if __name__ == '__main__':
     base10=base_conversion(2756)
