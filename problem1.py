list = []
sum = 0
i = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        list.append(i)
    i+=1
for x in list:
    sum += x
print(sum)
