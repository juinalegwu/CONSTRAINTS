def reverse_first(queue, k):
    return queue[:k][::-1] + queue[k:]

print(reverse_first([10, 20, 30, 40, 50],3))
print(reverse_first([1, 2, 3, 4],2))
