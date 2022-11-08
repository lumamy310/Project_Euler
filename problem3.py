#function to identify not prime numbers
def isNotPrime(num):
    for z in range(2, num):
        if num % z == 0:
            return True
    else:
            return False


i = 600851475143
factors = []
#find factors and add to list
for z in range (1, i+1):
    if i % z == 0:
        factors.append(z)

primefactors = []
#remove non prime factors
for x in factors:
    if isNotPrime(x) == False:
        primefactors.append(x)


print(factors)
print(primefactors)
