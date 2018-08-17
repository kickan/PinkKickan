
startnum = int(input("Enter starting number: "))
endnum = int(input("Enter ending number: "))

#for i in range(startnum, endnum + 1, 1):
    #print (i)

def func(startnum, endnum):
    if startnum < endnum:
        for i in range(startnum, endnum + 1,1):
            print(i)
    elif startnum > endnum:
        for i in range(startnum, endnum - 1, -1):
            print(i)
func(startnum, endnum)
