numbers = [5, 12, 3, 8, 16,123,134,171,22,20,11,4, 9, 10, 22]
filtered = filter(lambda number:number > 10 and number%2==0, numbers)
print(list(filtered))
