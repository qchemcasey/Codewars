def find_it(seq):
    return next (x for x in seq if seq.count(x) % 2 != 0)

print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))