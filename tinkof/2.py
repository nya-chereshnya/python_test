numberOfCars = int(input())
if numberOfCars >= 1 and numberOfCars <= 10**5:
    cars = []
    invalidValue = False
    for car in range(numberOfCars):
        speed = int(input())
        if speed >= 1 and speed <= 10**9:
            cars.append(speed)
        else:
            invalidValue = True
    if invalidValue == False:
        for car in range(len(cars) - 1):
            if cars[car + 1] > cars[car]:
                cars[car + 1] = cars[car]
        print(*cars)