def split_string(s):
    if s == '':
        return ['']
    else:
        return s.split()
print(split_string(s))


# Better Solution   
def split_string(s):
    return s.split('')