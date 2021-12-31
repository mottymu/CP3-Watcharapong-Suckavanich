# Break and Continue Example

for x in range(12):
    for y in range(12):
        print(x + 1, "x", y + 1, "=", (x + 1) * (y + 1))
    break                                                   # break loop x
print("----------")

for x in range(12):
    for y in range(12):
        print(x + 1, "x", y + 1, "=", (x + 1) * (y + 1))
        break                                               # break loop y
print("----------")

for val in "hello ":
    if val == "l":
        continue                                            # skip if find "l"
    print(val)

print("The End")

