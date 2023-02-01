n = int(input())
if n >= 1 and n <= 50:
    if n % 3 == 0:
        print(int(2**(n / 3)))
    else:
        print(0)