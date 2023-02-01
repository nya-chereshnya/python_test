n = int(input())
if n >= 1 and n <= 10**5:
    maxDividend = 0
    maxNOD = 0
    for number in range(1, n + 1):
        NOD = 0
        dividend = 0
        for divider in range(1, number + 1):
            if number % divider == 0:
                NOD += 1
                dividend = number
            else:
                continue
        if NOD >= maxNOD:
            maxNOD = NOD
            maxDividend = divider
    print(maxDividend)
    print(maxNOD)
