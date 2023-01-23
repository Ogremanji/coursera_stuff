def sum_positive_numbers(n):
    print("debug point: n = ", n)
    n -= 1
    if n > 0:
        n += sum_positive_numbers(n)
    return n+1

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
