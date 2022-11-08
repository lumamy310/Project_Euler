def isPalindrome(num):
    if num//100000 == num%10 and num//10000%10 == num//10%10 and num//1000%10 == num//100%10:
        return True
    else:
        return False

#generate and check combinations of palindromes
maxproduct = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        product = a*b
        if isPalindrome(product) and product > maxproduct:
            maxproduct = product

print(maxproduct)