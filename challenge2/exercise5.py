def most_frequent(numbers):
    if not numbers:
        return None
    return max(set(numbers), key=numbers.count)
print(most_frequent([2, 5, 2, 8, 2, 5]))
print(most_frequent([4, 7, 7, 4]))
print(most_frequent([]))
