checklist = [11, 13, 14, 16, 17, 18, 19, 20]
def isDivisible(num):
    for z in checklist:
        if num % z == 0:
            continue
        else:
            return False
    return True

smallest = 0
for x in range(2520, 999999999):
    if isDivisible(x):
        smallest = x
        break

print(smallest)

