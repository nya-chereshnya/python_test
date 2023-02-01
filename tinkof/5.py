n = int(input())
if n >= 1 and n <= 10**5:
    sequenceOfNumders = []
    for i in range(1, n + 1):
        sequenceOfNumders.append(i)
    sequenceOfNumders.sort(reverse=True)
    if sum(sequenceOfNumders) % 3 == 0 and n > 3:
        controleSum = int(sum(sequenceOfNumders) / 3)
        print(controleSum, " - controle sum")
        for round in range(2):
            blockOfNumbers = []
            for number in sequenceOfNumders:
                if sum(blockOfNumbers) + number < controleSum:
                    blockOfNumbers.append(number)
                    sequenceOfNumders.remove(number)
                elif sum(blockOfNumbers) + number == controleSum:
                    blockOfNumbers.append(number)
                    sequenceOfNumders.remove(number)
                    break
                elif sum(blockOfNumbers) + number > controleSum:
                    continue
            print(len(blockOfNumbers))
            print(*blockOfNumbers, "\n")
            print(sum(blockOfNumbers), " - sum")
        print(len(sequenceOfNumders))
        print(*sequenceOfNumders, "\n")
        print(sum(sequenceOfNumders), " - sum")
    else:
        print(-1)