from itertools import cycle

numbers = (str(input("insert your numbers: ")))
#hitta summan av alla nummer som matchar nästa siffra
num = []
nynum=[]

for x in range(len(numbers)):
    num.append(int(numbers[x]))

cyclenum = cycle(num)
print(num)

for i in range(len(cyclenum + 1):
    if cyclenum[i] == next(cyclenum[i]):
       nynum.append(cyclenum[i])

summa = sum(nynum)
print(nynum)
print(summa)

