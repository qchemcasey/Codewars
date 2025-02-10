def positive_sum(arr):
    positive = []
    for x in arr:
        if int(x) >= 0:
            positive.append(x)
    return sum(positive)

# Best Solution

def positive_sum(arr):
    return sum(x for x in arr if x > 0)