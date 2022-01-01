# Tuple Example

tupleExample = ('AA', 'BB', 'CC')
print(tupleExample)
tupleExample2 = ('DD', 'EE')
print(tupleExample2)
tupleExample3 = tupleExample + tupleExample2
print(tupleExample3)
print(tupleExample3[3])
print(tupleExample3[:3])
print('BB' in tupleExample3)
print('ZZ' in tupleExample3)

for i in tupleExample3:
    print("Hello", i)