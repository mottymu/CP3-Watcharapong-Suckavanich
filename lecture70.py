# Dictionary Example 2

words = {'Bird': 'มันคือนก', 'Dog': 'มันคือสุนัข', 'Cat': 'มันคือแมว', 'Fish': 'มันคือปลา', 'Ant': 'มันคือมด'}
print(words)
print(words['Bird'])
print(words.items())
print(words.keys())
print(words.values())
print(type(words.keys()))
for i in words.keys():
    print(i)
for i in words.values():
    print(i)