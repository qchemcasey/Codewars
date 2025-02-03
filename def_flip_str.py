def solution(string):
    lst = list(string)
    flip = lst[-1::-1] 
    reverse = ''.join(flip)
    return reverse

print(solution("hello"))