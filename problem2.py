n1 = 1
n2 = 2
n = 0
z=2
while n < 4000000:
    n = n1 + n2
    if n % 2 == 0:
        z += n
    n1 = n2
    n2 = n
print(z)
