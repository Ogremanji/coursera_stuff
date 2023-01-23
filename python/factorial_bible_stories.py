def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * n
        n = n-1
    return result

#print(factorial(7))

for n in range(0,9):
    print(n, factorial(n+1))
