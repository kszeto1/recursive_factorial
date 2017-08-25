# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    base = 1
    total = 1
    range_of_n = range(1, n + 1)
    for numbers in range_of_n:
        if numbers == 2:
            total = numbers * (numbers - 1)
        else:
            total *= numbers
    return total
    if n == 0:
        return base





print factorial(0)
#>>> 1

print factorial(5)
#>>> 120

print factorial(10)
#>>> 3628800