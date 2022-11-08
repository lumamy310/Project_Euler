sumsquares = 0
squaressum = 0
for x in range(1, 101):
    sumsquares += x**2

total = 0
for z in range(1, 101):
    total += z

squaressum = total**2

print(squaressum - sumsquares)
