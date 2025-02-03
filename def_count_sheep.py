def count_sheeps(sheep):
    x = 0
    for i in sheep:
        if i == True:
            x += 1
        else:
            pass
    return x 

# Better solution
def count_sheeps(sheep):
    return sheep.count(True)
