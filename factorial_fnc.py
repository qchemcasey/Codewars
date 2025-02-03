def summation(num):
    x = 0    
    count = []
    while x != num:
        x += 1
        count.append(x)
    return(sum(count))
    
# Better Solution

def summation(num):
    return sum(range(1, num + 1))