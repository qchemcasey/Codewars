def remove_char(s):
    lst = list(s)
    lst.pop(0)
    lst.pop()
    return ''.join(lst)

# Better solution

def remove_char(s):
    return s[1 : -1]