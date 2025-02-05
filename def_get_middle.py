def get_middle(s):

    if len(s)%2 == 0:
        mid = (len(s)/2) - 1
        return s[int(mid):int(mid+2)]
    else:
        mid = (len(s) - 1)/2
        return s[int(mid)]
    
print(get_middle("testy"))