def reverse_seq(n):
    arr = list(range(1,n+1))
    return arr[::-1]

# Best Solution
def reverse_seq(n):
    return list(range(n, 0, -1))