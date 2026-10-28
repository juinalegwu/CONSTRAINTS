def count_occurences(numbers, target):
    count = 0 
    for number in numbers:
        if number == target:
           count = count + 1
    return count
print(count_occurences([2, 5, 2, 8, 2],2))
print(count_occurences([1, 4, 7],10))