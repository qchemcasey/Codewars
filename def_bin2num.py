def binary_array_to_number(arr):
    s = ''.join(str(x) for x in arr)
    return int(s,2)