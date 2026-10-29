def move_zeros(numbers):
    position = 0

    for number in numbers:
        if number != 0:
            numbers[position] = number
            position += 1

    while position < len(numbers):
        numbers[position] = 0
        position += 1

    return numbers
 
print(move_zeros([1, 3, 12, 0, 0])) 
print(move_zeros([4, 5, 2, 0, 0]))
print(move_zeros([1, 2, 3]))