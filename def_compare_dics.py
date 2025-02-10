def cakes(recipe, available):
    return min(available.get(i, 0) // recipe[i] for i in recipe)

print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))