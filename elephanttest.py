#make algorithm that returns the index of a given number if it is in a list

list = [4, 7, 4, 3, 9]

for i in range(len(list)):
    if list[i] == 9:
        print(i + 1)

list2 = [1, 2, 9, 4, 7] #skapar lista

#sätter found till false då inget ännu hittats
found = False

# för varje plats i listan går ett varv i loopen
for i in range(len(list2)):
    # Om siffran på plats i är 6 ändras found till true och platsen skrivs ut
    if list[i] == 6:
        found = True
        print(i + 1)

#Om found inte har ändrats till true är den fortfarande false och ingen siffra har hittats
# att siffran inte kan hittas skrivs ut.
if found == False:
    print("this number cant be found")
