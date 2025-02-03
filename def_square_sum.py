def square_sum(numbers):
    squared = []
    for value in numbers:
        value = value**2
        squared.append(value)
    return sum(squared)

# Better Solution
def square_sum(numbers):
    return sum(x**2 for x in numbers)