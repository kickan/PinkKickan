# Be om siffror
numbers = (input("insert your numbers: "))

# gör om numbers till lista

num = []
for x in range(len(numbers)):
    num.append(int(numbers[x]))

#lägg till första siffran igen på slutet

num.append(num[0])
print(num)

#gör ny lista
nynum=[]

for i in range(len(num) -1):
    if num[i] == num[i +1]:
       nynum.append(num[i])

summa = sum(nynum)
print(nynum)
print(summa)