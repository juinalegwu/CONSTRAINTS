def first_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

print(first_position([2, 4, 4, 4, 8, 10],4))
print(first_position([1, 3, 5, 7],6))
