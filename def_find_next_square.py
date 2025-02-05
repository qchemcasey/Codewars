def find_next_square(sq):
    if int(sq**(1/2)) != (sq**(1/2)):
        return -1
    else:
        return ((sq**(1/2))+1)**2
