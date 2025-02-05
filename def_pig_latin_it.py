def pig_it(text):
    lst = text.split()
    latin = []
    for i in lst:
        i = i[1:] + i[0] + 'ay' if i.isalpha() else i
        latin.append(i)
    return ' '.join(latin)

print(pig_it('Pig latin is cool'))

# Best Solution

def pig_latin_it(phrase):
    lst = phrase.split()
    return ' '.join( [i[1:] + i[:1] + 'ay' if i.isalpha() else i for i in lst])

print(pig_latin_it('Pig latin is cool'))