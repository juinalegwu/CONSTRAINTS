def closest_numbers(numbers,target):
    closest = numbers[0]
    min_diff = abs(closest - target)
    for i in range(len(numbers)):
        diff = abs(numbers[i] - target)
        if diff < min_diff:
            min_diff = diff
            closest = numbers[i]
    return closest 

print(closest_numbers([4, 8, 15, 20],13))
print(closest_numbers([8, 12],10))