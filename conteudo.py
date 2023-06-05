def sum_array(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum


def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares


def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result


# Os arrays têm sempre o mesmo tamanho
def multiply_more_arrays(array1, array2, array3):
    result = []
    for number1 in array1:
        for number2 in array2:
            for number3 in array3:
                result.append(number1 + number2 + number3)

    return result


def multiply_arrays(array1, array2, array3):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            for number3 in array3:
                print(f'Array 3: {number3}')
                result.append(number1 * number2)
                number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = [1, 2, 3, 4, 5]

multiply_arrays(meu_array, meu_array, meu_array)


# print(multiply_arrays([15, 10, 6, 8], [2, 5, 2]))
