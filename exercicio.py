import random


def randomAverage(n):
    array_list = []

    for _ in range(100):
        average = 0
        for _ in range(n):
            average += random.randrange(1, n)
        average = average / n
        array_list.append(average)
    return array_list


print(randomAverage(10))
