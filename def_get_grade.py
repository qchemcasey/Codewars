def get_grade(s1, s2, s3):
    x = (s1 + s2 + s3) / 3
    if x >= 90:
        return "A"
    elif 80 <= x < 90: 
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 60 <= x < 70:
        return "D"
    else:
        return "F"

print(get_grade(95, 90, 93))